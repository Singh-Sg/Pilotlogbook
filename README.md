PilotLogbook

# Project Overview
This project is designed to efficiently handle data import and export processes. It imports data from the file provides by the user, stores the imported data in Django models, and then exports the data from these models, converting it into a CSV file named `export-logbook_template.csv`.


# Project Setup
python version = 3.9

1. Create virtual-environment

    .If virtualenv is installed
        virtualenv -p python(your python version) environment-name
    .If virtualenv is not installed, install this using pip install virtualenv

2. Activate Virtualenv

    .source environment-name/bin/activate

3. Install requirements.txt

    .pip3 install -r requirements.txt

4. Run migration and migrate command:

    .python manage.py makemigrations
    .python manage.py migrate
    .Create super user for admin panel by filling required details
        python manage.py createsuperuser

5. Run Project Using - python manage.py runserver