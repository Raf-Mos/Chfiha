# Generated by Django 4.2.13 on 2024-07-08 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_service_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price_basic_description',
            field=models.CharField(default='Basic plan description', max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='price_premium_description',
            field=models.CharField(default='Premium plan description', max_length=200),
        ),
        migrations.AddField(
            model_name='service',
            name='price_standard_description',
            field=models.CharField(default='Standard plan description', max_length=200),
        ),
        migrations.AlterField(
            model_name='service',
            name='features',
            field=models.JSONField(default=list, help_text='List of features'),
        ),
    ]
