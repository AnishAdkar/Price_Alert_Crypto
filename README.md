
## Requirements

- Python 3.9
- Django
- Django REST Framework
- Celery
- requests

## Setup Instructions

1. Clone the Repository

2. Open Git Desktop and use "open repository in VS Code".

3. Change directory to 'Price_Alert_App' within 'Price_Alert_App'.
   i.e. Use "cd price_alert_app" command in bash.

4. On bash terminal, Run Command 'docker-compose up --build' to Run Django server.

5. Use Postman to interact with REST API.

   How to use Postman :

   1. Obtain a JWT Token.
      - Set the request type to POST.
      - Set the URL to http://127.0.0.1:8000/api/token/.
      - Go to the "Body" tab, select "raw", and set the format to JSON.
      - Enter to send :

      {
          "username": "user1",
          "password": "user1"
      }

      -Receive :

      {
          "refresh": "your_refresh_token",
          "access": "your_access_token"
      }

      
   2. Creating Alert :
      - Create a new POST request.
      - Set the URL to http://127.0.0.1:8000/alerts/create/.
      - Go to the "Authorization" tab, select "Bearer Token", and paste your access token.
      - Go to the "Body" tab, select "raw", and set the format to JSON.
      - Enter to Send:

      {
        "user":"1",
        "cryptocurrency": "BTC",
        "target_price": "33000.00"
      }

      - (Do not Change the user value)

   3. List All Alerts:
      - Create a new GET request.
      - Set the URL to http://127.0.0.1:8000/alerts/list/.
      - Go to the "Authorization" tab, select "Bearer Token", and paste your access token.
      - Send the request. You should receive a list of alerts.

   4. Delete an Alert:
      - Create a new DELETE request.
      - Set the URL to http://127.0.0.1:8000/alerts/delete/<alert_id>/ (replace <alert_id> with the actual ID of the alert you want to delete).
      - Go to the "Authorization" tab, select "Bearer Token", and paste your access token.
      - Send the request. 

      
   
