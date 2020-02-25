from rest_framework import serializers
from .models import ItemType, AcqItem


class ItemTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemType
        fields = ['id', 'itype']


class AcqItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcqItem
        fields = ['id', 'iname', 'iprice', 'idescription', 'itype']
