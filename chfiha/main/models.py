from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='static/profile_pictures/', default='static/profile_pictures/9334228.jpg')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')

    def __str__(self):
        return self.user.email


class Categorie(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()

    def __str__(self):
        return self.title

    @staticmethod
    def get_default_category():
        default_category, created = Categorie.objects.get_or_create(title='Default', description='Default category')
        return default_category.id


class Service(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=False, default=Categorie.get_default_category)
    title = models.CharField(max_length=200, default="Service Title")
    description = models.TextField()
    features = models.JSONField(default=list, help_text="List of features")
    detailed_description = models.TextField(default="")
    freelancer = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'freelancer'})
    price_essential = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    price_essential_description = models.CharField(max_length=200, default="Essential plan description")
    duration_days = models.IntegerField(default=1, help_text="Duration of the service in days")

    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Project(models.Model):
    STATUS_CHOICES = [
        ('D', 'Delivered'),
        ('I', 'In Progress'),
        ('P', 'Pending'),
    ]

    client = models.ForeignKey(Profile, related_name='client_projects', on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'user_type': 'client'})
    freelancer = models.ForeignKey(Profile, related_name='freelancer_projects', on_delete=models.CASCADE, limit_choices_to={'user_type': 'freelancer'}, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()

    step1_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    step1_file = models.FileField(upload_to='static/project_files/step1', blank=True, null=True)
    step2_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    step2_file = models.FileField(upload_to='static/project_files/step2', blank=True, null=True)
    step3_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    step3_file = models.FileField(upload_to='static/project_files/step3', blank=True, null=True)
    step4_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    step4_file = models.FileField(upload_to='static/project_files/step4', blank=True, null=True)
    step5_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    step5_file = models.FileField(upload_to='static/project_files/step5', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.freelancer:
            self.freelancer = self.service.freelancer

        self.end_date = self.start_date + timedelta(days=self.service.duration_days)
        self.price = self.service.price_essential
        super().save(*args, **kwargs)

class OrderMessage(models.Model):
    sender = models.ForeignKey(Profile, related_name='message_sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='message_receiver', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='static/order_message_files/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.client.username} for {self.project.service.name}"
