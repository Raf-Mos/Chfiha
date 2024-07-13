from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='static/profile_pictures/', default='static/profile_pictures/9334228.jpg')
    is_client = models.BooleanField(default=True)
    is_freelancer = models.BooleanField(default=False)

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
    price_basic = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    price_basic_description = models.CharField(max_length=200, default="Basic plan description")

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

    order_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    client = models.ForeignKey(Profile, related_name='client_projects', on_delete=models.CASCADE, null=True, blank=True)
    freelancer = models.ForeignKey(Profile, related_name='freelancer_projects', on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    step1_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    step1_file = models.FileField(upload_to='project_files/step1', blank=True, null=True)
    step2_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    step2_file = models.FileField(upload_to='project_files/step2', blank=True, null=True)
    step3_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    step3_file = models.FileField(upload_to='project_files/step3', blank=True, null=True)
    step4_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    step4_file = models.FileField(upload_to='project_files/step4', blank=True, null=True)
    step5_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    step5_file = models.FileField(upload_to='project_files/step5', blank=True, null=True)


class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.client.username} for {self.project.service.name}"
