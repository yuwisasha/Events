from django.db import models


class Organization(models.Model):
    
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    address = models.CharField(
        max_length=255,
    )
    postcode = models.PositiveIntegerField()

    def __str__(self):
        return self.title
