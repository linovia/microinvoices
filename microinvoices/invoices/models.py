from django.db import models
from django.conf import settings


class Invoice(models.Model):
    name = models.CharField(max_length=256)
    additional_infos = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="invoices")
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
