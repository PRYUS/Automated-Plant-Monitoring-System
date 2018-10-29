from django.contrib import admin
from .models import sensorreadings,plant,common


# Register your models here.
admin.site.register(sensorreadings)
admin.site.register(plant)
admin.site.register(common)

