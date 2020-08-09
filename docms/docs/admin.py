from django.contrib import admin

from .models import Document, File, Fileset, Tag


admin.site.register((Document, File, Fileset, Tag))
