import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import CustomUser
from main.models import Profile, Service, Project, Review
import json


class Command(BaseCommand):
    help = 'Populate database with initial data for a development agency'

    def handle(self, *args, **kwargs):
        # Create users
        user1 = CustomUser.objects.create(first_name='kamal', last_name='miftah', email='user1@example.com', password='password')
        user2 = CustomUser.objects.create(first_name='youssef', last_name='ibba', email='user2@example.com', password='password')
        user3 = CustomUser.objects.create(first_name='mostafa', last_name='rafmos', email='user3@example.com', password='password')

        # Create profiles
        Profile.objects.create(user=user1, bio='Bio of user1')
        Profile.objects.create(user=user2, bio='Bio of user2')
        Profile.objects.create(user=user3, bio='Bio of user3')

        # Create services
        service1 = Service.objects.create(
            title='Web Development',
            description='Custom web application development',
            features=json.dumps(['Responsive design', 'Backend development', 'API integration']),
            price_basic=1000.00,
            price_standard=2000.00,
            price_premium=3000.00
        )

        service2 = Service.objects.create(
            title='Mobile App Development',
            description='iOS and Android app development',
            features=json.dumps(['Native app development', 'UI/UX design', 'Testing and deployment']),
            price_basic=1500.00,
            price_standard=2500.00,
            price_premium=3500.00
        )

        # Create projects
        project1 = Project.objects.create(
            client=user1,
            service=service1,
            description='Develop a custom web application for client X',
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=30),
            status='C'
        )

        project2 = Project.objects.create(
            client=user2,
            service=service2,
            description='Create an iOS and Android app for client Y',
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=60),
            status='I'
        )

        # Create reviews
        Review.objects.create(
            project=project1,
            client=user1,
            rating=random.randint(1, 5),
            comment='Great job on the web app!'
        )

        Review.objects.create(
            project=project2,
            client=user2,
            rating=random.randint(1, 5),
            comment='The app looks promising!'
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))

