# Generated by Django 5.0.6 on 2024-07-09 20:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_service_price_basic_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.AddField(
            model_name='profile',
            name='is_client',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_freelancer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='freelancer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='freelancer_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='order_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='project',
            name='step1_file',
            field=models.FileField(blank=True, null=True, upload_to='project_files/step1'),
        ),
        migrations.AddField(
            model_name='project',
            name='step1_status',
            field=models.CharField(choices=[('D', 'Delivered'), ('I', 'In Progress'), ('P', 'Pending')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='project',
            name='step2_file',
            field=models.FileField(blank=True, null=True, upload_to='project_files/step2'),
        ),
        migrations.AddField(
            model_name='project',
            name='step2_status',
            field=models.CharField(choices=[('D', 'Delivered'), ('I', 'In Progress'), ('P', 'Pending')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='project',
            name='step3_file',
            field=models.FileField(blank=True, null=True, upload_to='project_files/step3'),
        ),
        migrations.AddField(
            model_name='project',
            name='step3_status',
            field=models.CharField(choices=[('D', 'Delivered'), ('I', 'In Progress'), ('P', 'Pending')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='project',
            name='step4_file',
            field=models.FileField(blank=True, null=True, upload_to='project_files/step4'),
        ),
        migrations.AddField(
            model_name='project',
            name='step4_status',
            field=models.CharField(choices=[('D', 'Delivered'), ('I', 'In Progress'), ('P', 'Pending')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='project',
            name='step5_file',
            field=models.FileField(blank=True, null=True, upload_to='project_files/step5'),
        ),
        migrations.AddField(
            model_name='project',
            name='step5_status',
            field=models.CharField(choices=[('D', 'Delivered'), ('I', 'In Progress'), ('P', 'Pending')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/profile_pictures/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]