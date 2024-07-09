from django.contrib import admin
from .models import Service, Profile, Project

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture', 'is_client', 'is_freelancer')
    list_filter = ('is_client', 'is_freelancer')
    search_fields = ('user__email',)

admin.site.register(Profile, ProfileAdmin)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_basic', 'price_standard', 'price_premium')
    search_fields = ('title', 'description')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'client', 'freelancer', 'service', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('order_number', 'client__username', 'freelancer__username', 'service__title')

    fieldsets = (
        (None, {
            'fields': ('order_number', 'client', 'freelancer', 'service', 'description', 'start_date', 'end_date', 'status')
        }),
        ('Delivery Steps', {
            'fields': ('step1_completed', 'step1_file', 'step2_completed', 'step2_file', 'step3_completed', 'step3_file', 'step4_completed', 'step4_file', 'step5_completed', 'step5_file')
        }),
    )

admin.site.register(Project, ProjectAdmin)

