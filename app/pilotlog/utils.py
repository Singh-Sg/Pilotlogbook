import json
from django.apps import apps
from .models import BaseModel
from django.db import models
import csv
from django.http import HttpResponse
from datetime import datetime
from django.utils import timezone
from .models import *

TABLE_MAP = {
    "aircraft": "Aircraft",
    "airfield": "Airfield",
    "settingconfig": "SettingConfig",
    "flight": "Flight",
    "imagepic": "ImagePic",
    "limitrules": "LimitRules",
    "myquery": "MyQuery",
    "myquerybuild": "MyQueryBuild",
    "pilot": "Pilot",
    "qualification": "Qualification",
}


def import_data(file_path):
    # Open the file at the specified path with UTF-8 encoding
    with open(file_path, "r", encoding="utf-8") as file:
        raw_data = file.read()

    # Replace escaped quotes with actual quotes in the raw data
    unescaped_data = raw_data.replace(r"\"", '"')

    # Parse the JSON data
    data = json.loads(unescaped_data)
    table_data = {}
    # Iterate through each item in the data
    for item in data:
        table_name = item.get("table")
        meta_data = item.get("meta")
        model_data = []  # List to hold model instances for bulk creation

        # Skip processing if table_name or meta_data is missing
        if not table_name or not meta_data:
            print(f"Invalid data: {item}")
            continue

        try:
            # Dynamically get the model class using the table_name
            ModelClass = apps.get_model("pilotlog", table_name)
            instance = ModelClass()  # Create an empty instance of the model
            # Get all DateTimeFields in the model
            datetime_fields = {
                field.name: field
                for field in ModelClass._meta.fields
                if isinstance(field, models.DateTimeField)
            }
            # Set values for fields directly from the item data
            for field_name, value in item.items():
                if field_name in datetime_fields and isinstance(value, int):
                    # Convert timestamp to aware datetime
                    naive_dt = datetime.fromtimestamp(value)
                    value = timezone.make_aware(
                        naive_dt, timezone.get_current_timezone()
                    )

                # Set the value if the field exists in the model
                if hasattr(ModelClass, field_name):
                    setattr(instance, field_name, value)

            # Set values for fields from the meta_data
            for field_name, value in meta_data.items():
                # Convert field name to lowercase if necessary and check if the field exists
                field_name = (
                    field_name
                    if hasattr(ModelClass, field_name)
                    else field_name.lower()
                )
                try:
                    # Handle empty strings by setting them to None
                    if isinstance(value, str) and not value:
                        value = None
                    # Convert record_modified timestamp to aware datetime
                    elif field_name in datetime_fields and isinstance(value, int):
                        naive_dt = datetime.fromtimestamp(value)
                        value = timezone.make_aware(
                            naive_dt, timezone.get_current_timezone()
                        )

                    # Set the value if the field exists in the model
                    if hasattr(ModelClass, field_name):
                        setattr(instance, field_name, value)
                except Exception as e:
                    print("error : ", e)

            # Add the instance to the list for bulk creation
            model_data.append(instance)
            table_name = TABLE_MAP.get(table_name.lower())
            if table_data.get(table_name):
                table_data[table_name].append(instance)
            else:
                table_data[table_name] = [instance]
        except Exception as e:
            print(f"Error processing item {item}: {e}")

        # Bulk create all instances if the model class is found
        # if ModelClass:
        #     try:
        #         # ModelClass.objects.bulk_create(model_data)
        #         pass
        #     except Exception as e:
        #         print("error : ", e)
    return table_data


def export_data_to_csv(filename="export-logbook_template.csv"):
    # Create an HTTP response with CSV content type
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    # Initialize the CSV writer
    writer = csv.writer(response)

    # Get all installed models
    models = apps.get_models()

    # Create a CSV file for each model that is not abstract and is a subclass of BaseModel
    for model in models:
        if not model._meta.abstract and issubclass(model, BaseModel):
            model_name = model._meta.model_name
            Model_fields = [field.name.capitalize() for field in model._meta.fields]
            Model_name = model_name.capitalize()

            # Write model name as a header
            writer.writerow([f"{Model_name} Table"])
            writer.writerow(Model_fields)  # Write the header for the fields

            # Write data for each instance of the model
            model_fields = [field.name for field in model._meta.fields]
            instances = model.objects.all()
            for instance in instances:
                # Write each field value to the CSV row
                row = [getattr(instance, field, "") for field in model_fields]
                writer.writerow(row)

            # Add a blank line
            writer.writerow([])
            writer.writerow([])

    return response
