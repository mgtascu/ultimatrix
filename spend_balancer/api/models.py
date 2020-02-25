from django.db import models


class ItemType(models.Model):
    itype = models.CharField(max_length=50, null=False)


class AcqItem(models.Model):
    iname = models.CharField(max_length=200, null=False)
    iprice = models.FloatField(null=True)
    idescription = models.CharField(max_length=3000, null=True)
    itype = models.ForeignKey(ItemType, on_delete=models.CASCADE)
