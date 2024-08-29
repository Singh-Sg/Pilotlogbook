from rest_framework import serializers
from app.pilotlog.models import (
    Aircraft,
    Airfield,
    SettingConfig,
    Flight,
    ImagePic,
    LimitRules,
    MyQuery,
    MyQueryBuild,
    Pilot,
    Qualification,
)


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = "__all__"


class AirfieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airfield
        fields = "__all__"


class SettingConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingConfig
        fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


class ImagePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePic
        fields = "__all__"


class LimitRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LimitRules
        fields = "__all__"


class MyQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyQuery
        fields = "__all__"


class MyQueryBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyQueryBuild
        fields = "__all__"


class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = "__all__"


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"
