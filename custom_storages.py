from django.conf import settings

# Import S3Boto3Storage class from django-storages which interfaces with S3
from storages.backends.s3boto3 import S3Boto3Storage


# For static files.
class StaticStorage(S3Boto3Storage):
    """
    A storage backend for static files using Amazon S3.

    This class inherits from S3Boto3Storage and specifies the location
    within the S3 bucket where static files are stored. The location
    is defined in the Django settings, allowing for easy configuration
    of where static files are served from.

    Attributes:
        location (str): The path within the S3 bucket where static files
        are stored, configured via `STATICFILES_LOCATION`
        in Django settings.
    """

    location = settings.STATICFILES_LOCATION


# For media files (like user-uploaded files)
class MediaStorage(S3Boto3Storage):
    """
    A storage backend for media files using Amazon S3.

    This class inherits from S3Boto3Storage and specifies the location
    within the S3 bucket where media files, such as user-uploaded content,
    are stored. The location is defined in the Django settings, enabling
    straightforward management of media files in the S3 storage system.

    Attributes:
        location (str): The path within the S3 bucket where media files are
        stored, configured via `MEDIAFILES_LOCATION` in Django settings.
    """

    location = settings.MEDIAFILES_LOCATION
