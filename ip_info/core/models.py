from django.db import models


class IPv4GeoDataModel(models.Model):
    id = models.AutoField(primary_key=True)
    ipv4 = models.CharField(max_length="15", blank=False, unique=True)
    country = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    latitude = models.CharField(max_length=255, blank=True)
    longitude = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.ipv4