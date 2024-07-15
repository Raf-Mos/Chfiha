from django.contrib import admin
from .models import Service, Profile, Project, OrderMessage, Categorie

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture', 'user_type')
    list_filter = ('user_type',)
    search_fields = ('user__email',)

admin.site.register(Profile, ProfileAdmin)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_essential', 'duration_days')
    search_fields = ('title', 'description')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('client', 'freelancer', 'service', 'start_date', 'end_date')
    search_fields = ('client__email', 'freelancer__email', 'service__title')
    list_filter = ('start_date', 'end_date')
    fieldsets = (
        (None, {
            'fields': ('client', 'freelancer', 'service', 'start_date', 'end_date', 'price', 'transaction_id', 'payment_status', 'payer_email')
        }),
        ('Delivery Steps', {
            'fields': (
                ('step1_status', 'step1_file'),
                ('step2_status', 'step2_file'),
                ('step3_status', 'step3_file'),
                ('step4_status', 'step4_file'),
                ('step5_status', 'step5_file'),
            )
        }),
    )

admin.site.register(Project, ProjectAdmin)

admin.site.register(OrderMessage)

admin.site.register(Categorie)
