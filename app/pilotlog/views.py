from .utils import import_data
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class DataViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        try:
            # Attempt to import data from the specified JSON file
            model_file = request.FILES.get("table_file")
            if not model_file:
                return Response({'error': "Provide table_file"}, status=status.HTTP_404_NOT_FOUND)
            save_path = os.path.join(settings.MEDIA_ROOT, model_file.name)
            path = default_storage.save(save_path, ContentFile(model_file.read()))
         
            data = import_data(save_path)
            if default_storage.exists(save_path):
                default_storage.delete(save_path)
            return Response({"message": "Data imported successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            # If an error occurs, return a 500 response with the error message
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)