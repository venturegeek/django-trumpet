from django.apps import AppConfig
from django.db.models.signals import post_save

from trumpet import update_bucket_version


class TrumpetConfig(AppConfig):
    name = 'trumpet'

