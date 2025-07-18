from django.contrib import admin
from .models import Country, Region
# Register your models here.
admin.site.register([Country, Region])