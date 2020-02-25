from django.contrib import admin

from .models import ItemType, AcqItem

admin.site.register(ItemType)
admin.site.register(AcqItem)
