from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import DataBucket
from .serializers import DataBucketSerializer


@api_view(['GET'])
def list_all_buckets(request):
    """
    List All Data Buckets.
    """

    buckets = DataBucket.objects.all()
    serializer = DataBucketSerializer(buckets, many=True)

    return Response(serializer.data)