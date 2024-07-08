from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.email

class Service(models.Model):
    title = models.CharField(max_length=200, default="Service Title")
    description = models.TextField()
    features = models.JSONField(default=list, help_text="List of features")
    detailed_description = models.TextField(default="")
    price_basic = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    price_basic_description = models.CharField(max_length=200, default="Basic plan description")
    price_standard = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    price_standard_description = models.CharField(max_length=200, default="Standard plan description")
    price_premium = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    price_premium_description = models.CharField(max_length=200, default="Premium plan description")

    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Project(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
    ]
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"{self.service.name} for {self.client.username}"

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.client.username} for {self.project.service.name}"

