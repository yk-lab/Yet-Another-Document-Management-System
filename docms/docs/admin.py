from django.contrib import admin

from .models import Document, File, Fileset


admin.site.register((Document, File, Fileset))
