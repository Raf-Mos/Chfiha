import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction
from accounts.models import CustomUser
from main.models import Profile, Service, Project, Review, Categorie
import json

class Command(BaseCommand):
    help = 'Populate database with initial data for a development agency'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                # Delete previous data
                CustomUser.objects.all().delete()
                Profile.objects.all().delete()
                Service.objects.all().delete()
                Project.objects.all().delete()
                Review.objects.all().delete()
                Categorie.objects.all().delete()

                # Create users
                user1 = CustomUser.objects.create_user(first_name='kamal', last_name='miftah', email='user1@example.com', password='password')
                user2 = CustomUser.objects.create_user(first_name='youssef', last_name='ibba', email='user2@example.com', password='password')
                user3 = CustomUser.objects.create_user(first_name='mostafa', last_name='rafmos', email='user3@example.com', password='password')

                # Define categories
                categories = [
                    {'title': 'Development', 'description': 'All development services'},
                    {'title': 'Marketing', 'description': 'All marketing services'},
                    {'title': 'Design', 'description': 'All design services'},
                    {'title': 'Consulting', 'description': 'All consulting services'}
                ]

                # Create categories
                created_categories = {}
                for cat_data in categories:
                    category = Categorie.objects.create(
                        title=cat_data['title'],
                        description=cat_data['description']
                    )
                    created_categories[cat_data['title']] = category

                # Define services
                services = [
                    {
                        'title': 'Web Development',
                        'categorie': created_categories['Development'],
                        'description': 'Custom web application development',
                        'features': ['Responsive design', 'Backend development', 'API integration'],
                        'detailed_description': 'Full web development services from start to finish.',
                        'price_basic': 1000.00,
                        'price_basic_description': 'Basic web development package'
                    },
                    {
                        'title': 'Mobile App Development',
                        'categorie': created_categories['Development'],
                        'description': 'iOS and Android app development',
                        'features': ['Native app development', 'UI/UX design', 'Testing and deployment'],
                        'detailed_description': 'Comprehensive mobile app development services.',
                        'price_basic': 1500.00,
                        'price_basic_description': 'Basic mobile app development package'
                    },
                    {
                        'title': 'SEO Services',
                        'categorie': created_categories['Marketing'],
                        'description': 'Improve your site ranking on search engines',
                        'features': ['Keyword research', 'On-page SEO', 'Link building'],
                        'detailed_description': 'Complete SEO services to boost your site’s visibility.',
                        'price_basic': 500.00,
                        'price_basic_description': 'Basic SEO package'
                    },
                    {
                        'title': 'Content Writing',
                        'categorie': created_categories['Marketing'],
                        'description': 'High-quality content for your website',
                        'features': ['Blog posts', 'Website content', 'Product descriptions'],
                        'detailed_description': 'Professional content writing services.',
                        'price_basic': 200.00,
                        'price_basic_description': 'Basic content writing package'
                    },
                    {
                        'title': 'Graphic Design',
                        'categorie': created_categories['Design'],
                        'description': 'Professional graphic design services',
                        'features': ['Logo design', 'Brochure design', 'Social media graphics'],
                        'detailed_description': 'Creative graphic design services.',
                        'price_basic': 300.00,
                        'price_basic_description': 'Basic graphic design package'
                    },
                    {
                        'title': 'Digital Marketing',
                        'categorie': created_categories['Marketing'],
                        'description': 'Comprehensive digital marketing services',
                        'features': ['Social media marketing', 'Email marketing', 'PPC advertising'],
                        'detailed_description': 'Effective digital marketing strategies.',
                        'price_basic': 800.00,
                        'price_basic_description': 'Basic digital marketing package'
                    },
                    {
                        'title': 'E-commerce Development',
                        'categorie': created_categories['Development'],
                        'description': 'Custom e-commerce solutions',
                        'features': ['Shopping cart integration', 'Payment gateway setup', 'Product management'],
                        'detailed_description': 'Complete e-commerce development services.',
                        'price_basic': 1200.00,
                        'price_basic_description': 'Basic e-commerce package'
                    },
                    {
                        'title': 'IT Consulting',
                        'categorie': created_categories['Consulting'],
                        'description': 'Expert IT consulting services',
                        'features': ['IT strategy development', 'System integration', 'Project management'],
                        'detailed_description': 'Professional IT consulting services.',
                        'price_basic': 1500.00,
                        'price_basic_description': 'Basic IT consulting package'
                    },
                    {
                        'title': 'Cloud Services',
                        'categorie': created_categories['Development'],
                        'description': 'Cloud computing solutions',
                        'features': ['Cloud migration', 'Cloud management', 'Cloud security'],
                        'detailed_description': 'Reliable cloud services for your business.',
                        'price_basic': 2000.00,
                        'price_basic_description': 'Basic cloud services package'
                    }
                ]

                # Create services
                for service_data in services:
                    Service.objects.create(
                        title=service_data['title'],
                        categorie=service_data['categorie'],
                        description=service_data['description'],
                        features=service_data['features'],
                        detailed_description=service_data['detailed_description'],
                        price_basic=service_data['price_basic'],
                        price_basic_description=service_data['price_basic_description']
                    )

                
                # Create projects
                project1 = Project.objects.create(
                    client=user1.profile,  # Assign Profile instance
                    service=Service.objects.get(title='Web Development'),
                    description='Develop a custom web application for client X',
                    start_date=timezone.now().date(),
                    end_date=timezone.now().date() + timezone.timedelta(days=30),
                    step1_status='C'
                )

                project2 = Project.objects.create(
                    client=user2.profile,  # Assign Profile instance
                    service=Service.objects.get(title='Mobile App Development'),
                    description='Create an iOS and Android app for client Y',
                    start_date=timezone.now().date(),
                    end_date=timezone.now().date() + timezone.timedelta(days=60),
                    step1_status='I'
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

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {e}'))
            raise

