from rest_framework import serializers
from .models import DataBucket


class DataBucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBucket
        fields = ['name', 'description', 'version', ]