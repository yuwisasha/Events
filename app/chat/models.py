from django.db import models

from users.models import User


class Message(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    message = models.TextField()

    def __str__(self):
        return self.message