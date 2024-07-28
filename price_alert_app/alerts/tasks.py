# alerts/tasks.py

from celery import shared_task
import requests
from django.core.mail import send_mail
from django.conf import settings
from .models import Alert

@shared_task
def fetch_prices():
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=ma', params={
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': 'false'
    })

    if response.status_code == 200:
        data = response.json()
        prices = {coin['symbol'].upper(): coin['current_price'] for coin in data}

        alerts = Alert.objects.filter(status='created')
        for alert in alerts:
            current_price = prices.get(alert.cryptocurrency.upper())
            if current_price and current_price >= alert.target_price:
                # Trigger the alert
                send_mail(
                    'Price Alert Triggered',
                    f'The price of {alert.cryptocurrency} has reached your target of {alert.target_price}',
                    settings.DEFAULT_FROM_EMAIL,
                    [alert.user.email],
                    fail_silently=False,
                )
                alert.status = 'triggered'
                alert.save()
    else:
        print('Failed to fetch prices')
