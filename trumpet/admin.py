from django.contrib import admin
from .models import DataBucket


class DataBucketAdmin(admin.ModelAdmin):
    list_display = ['description', 'name', 'version']


admin.site.register(DataBucket, DataBucketAdmin)