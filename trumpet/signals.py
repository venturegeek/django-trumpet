
from .models import DataBucket


def update_bucket_version(sender, **kwargs):

    MAGIC_PROPERTY = 'data_bucket'

    if hasattr(sender, MAGIC_PROPERTY) and getattr(sender, MAGIC_PROPERTY):
        bucket = getattr(sender, MAGIC_PROPERTY)

        try:
            db = DataBucket.objects.get(name=bucket)
        except DataBucket.DoesNotExist:
            db = DataBucket.objects.create(name=bucket, version=0)

        DataBucket.increment_version(db)


