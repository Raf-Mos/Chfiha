# Generated by Django 4.2.13 on 2024-07-08 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='category',
        ),
        migrations.RemoveField(
            model_name='service',
            name='name',
        ),
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.AddField(
            model_name='service',
            name='detailed_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='service',
            name='features',
            field=models.TextField(default='', help_text='List of features, separated by commas.'),
        ),
        migrations.AddField(
            model_name='service',
            name='price_basic',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='service',
            name='price_premium',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='service',
            name='price_standard',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='service',
            name='title',
            field=models.CharField(default='Service Title', max_length=200),
        ),
        migrations.DeleteModel(
            name='ServiceCategory',
        ),
    ]