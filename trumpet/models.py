from django.db import models
from django.db.models import F
from django.utils.translation import gettext_lazy as _


class DataBucket(models.Model):
    name = models.SlugField(max_length=250, help_text=_("Name of the bucket used in your Models."), unique=True)
    description = models.CharField(max_length=250, blank=True, null=True,
                                   help_text=_("Human readable description of what this bucket is."))
    version = models.IntegerField(default=0)

    @staticmethod
    def increment_version(db):
        DataBucket.objects.filter(pk=db.id).update(version=F('version') + 1)