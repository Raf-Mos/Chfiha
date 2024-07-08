from django.contrib import admin
from .models import Service
from .models import Profile

admin.site.register(Profile)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_basic', 'price_standard', 'price_premium')
    search_fields = ('title', 'description')
