from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

import uuid


class Dataset(ExportModelOperationsMixin("dataset"), models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    alias = models.TextField()


class IPv4GeoDataModel(models.Model):
    id = models.AutoField(primary_key=True)
    ipv4 = models.CharField(max_length=15, blank=False, unique=True)
    country = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    latitude = models.CharField(max_length=255, blank=True)
    longitude = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "IPv4GeoModel"
        verbose_name_plural = "IPv4GeoModels"

    def __str__(self):
        return self.ipv4