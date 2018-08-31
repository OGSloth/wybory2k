from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import MainCommune, Countries

admin.site.register(MainCommune)
admin.site.register(Countries)
