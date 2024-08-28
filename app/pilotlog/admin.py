from django.contrib import admin
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

admin.site.register(Aircraft)
admin.site.register(Airfield)
admin.site.register(SettingConfig)
admin.site.register(Flight)
admin.site.register(ImagePic)
admin.site.register(LimitRules)
admin.site.register(MyQuery)
admin.site.register(MyQueryBuild)
admin.site.register(Pilot)
admin.site.register(Qualification)
