from django.db import models
from django.utils.safestring import mark_safe

from organizations.models import Organization


def event_image_path(instance: models.Model, filename: str) -> str:
    # photo will be uploaded to MEDIA_ROOT/event_<id>/<filename>
    return "event_{0}/{1}".format(instance.title, filename)


class Event(models.Model):

    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(
        upload_to=event_image_path
    )
    date = models.DateField()

    def __str__(self):
        return self.title

    @mark_safe
    def image_preview(self):
        return mark_safe('<img src="{tag}" height="{height}" width="{width}" />' \
            .format(tag=self.image.url, height=self.image.height, width=self.image.width))