# Generated by Django 5.0.6 on 2024-07-16 21:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_merge_20240716_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='price_basic',
            new_name='price_essential',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_client',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_freelancer',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='order_number',
        ),
        migrations.RemoveField(
            model_name='service',
            name='price_basic_description',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('client', 'Client'), ('freelancer', 'Freelancer')], default='client', max_length=10),
        ),
        migrations.AddField(
            model_name='project',
            name='amount_paid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='payer_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='payment_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='project',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='duration_days',
            field=models.IntegerField(default=1, help_text='Duration of the service in days'),
        ),
        migrations.AddField(
            model_name='service',
            name='freelancer',
            field=models.ForeignKey(default=1, limit_choices_to={'user_type': 'freelancer'}, on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='price_essential_description',
            field=models.CharField(default='Essential plan description', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(blank=True, limit_choices_to={'user_type': 'client'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_projects', to='main.profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='freelancer',
            field=models.ForeignKey(blank=True, limit_choices_to={'user_type': 'freelancer'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='freelancer_projects', to='main.profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
