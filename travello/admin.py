import imp
from django.contrib import admin
from .models import destination,Detailed_desc
# Register your models here.

admin.site.register(destination)
admin.site.register(Detailed_desc)

