from django.urls import path
from .views import list_all_buckets

urlpatterns = [
    path('', list_all_buckets),
]