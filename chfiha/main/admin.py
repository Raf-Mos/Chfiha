from django.contrib import admin

# Register your models here.

from .models import ServiceCategory
from .models import Service
from .models import Profile

admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(Profile)
