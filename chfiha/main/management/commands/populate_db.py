# main/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from main.models import Profile, ServiceCategory, Service, Project
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Create a test user
        user = CustomUser.objects.create_user(username='testuser', password='testpass')

        # Create a profile for the user
        Profile.objects.create(user=user, bio='This is a test bio')

        # Create service categories
        web_dev = ServiceCategory.objects.create(name='Web Development', description='Web Development Services')
        mobile_dev = ServiceCategory.objects.create(name='Mobile Development', description='Mobile Development Services')

        # Create services
        service1 = Service.objects.create(category=web_dev, name='Website Design', description='Professional website design', price=1000.00)
        service2 = Service.objects.create(category=mobile_dev, name='Mobile App Development', description='Professional mobile app development', price=3000.00)

        # # Create projects
        # Project.objects.create(name='Website Project', description='Development of a new website', status='P', service=service1, start_date=date.today())
        # Project.objects.create(name='Mobile App Project', description='Development of a new mobile app', status='I', service=service2, start_date=date.today())

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))

