from .serializers import (
    AircraftSerializer,
    AirfieldSerializer,
    SettingConfigSerializer,
    FlightSerializer,
    ImagePicSerializer,
    LimitRulesSerializer,
    MyQuerySerializer,
    MyQueryBuildSerializer,
    PilotSerializer,
    QualificationSerializer,
)

# Create a mapping of model names to their serializers
SERIALIZER_MAP = {
    "aircraft": AircraftSerializer,
    "airfield": AirfieldSerializer,
    "settingconfig": SettingConfigSerializer,
    "flight": FlightSerializer,
    "imagepic": ImagePicSerializer,
    "limitrules": LimitRulesSerializer,
    "myquery": MyQuerySerializer,
    "myquerybuild": MyQueryBuildSerializer,
    "pilot": PilotSerializer,
    "qualification": QualificationSerializer,
}
