from django.contrib import admin
from .models import *


admin.site.register(Car)
admin.site.register(CarDetail)
admin.site.register(Detail)
admin.site.register(DetailType)
admin.site.register(DetailTypeProperty)
admin.site.register(DetailTypePropertyValue)
