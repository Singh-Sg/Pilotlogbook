from rest_framework import serializers
from .models import (
    Aircraft,
    Airfield,
    SettingConfig,
    Flight,
    ImagePic,
    LimitRules,
    MyQuery,
    MyQueryBuild,
    Pilot,
    Qualification
)


class AircraftTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'

class AirfieldTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airfield
        fields = '__all__'

class SettingConfigTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingConfig
        fields = '__all__'

class FlightTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class ImagePicTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePic
        fields = '__all__'

class LimitRulesTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = LimitRules
        fields = '__all__'

class MyQueryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyQuery
        fields = '__all__'

class MyQueryBuildTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyQueryBuild
        fields = '__all__'
   
class PilotTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = '__all__'

class QualificationTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'
