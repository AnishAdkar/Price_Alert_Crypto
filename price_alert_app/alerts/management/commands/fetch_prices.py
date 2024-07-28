# alerts/management/commands/fetch_prices.py

from django.core.management.base import BaseCommand
from alerts.tasks import fetch_prices

class Command(BaseCommand):
    help = 'Fetch cryptocurrency prices and check alerts'

    def handle(self, *args, **kwargs):
        fetch_prices.delay()  # Trigger the Celery task asynchronously
