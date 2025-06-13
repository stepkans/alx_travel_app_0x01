from django.core.management.base import BaseCommand
from listings.models import Listing, User
from django.contrib.auth import get_user_model
import random


class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        if not User.objects.exists():
            user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        else:
            user = User.objects.first()

        sample_locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret']
        for i in range(10):
            Listing.objects.create(
                title=f"Sample Listing {i+1}",
                description="This is a sample listing for testing purposes.",
                location=random.choice(sample_locations),
                price_per_night=random.uniform(50.0, 200.0),
                owner=user
            )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully with sample listings.'))
