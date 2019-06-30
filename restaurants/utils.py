import requests, json, os
from django.http import Http404
from .models import Restaurant


def call_api_with_key(location="San Francisco"):
    # Yelp authorization headers
    auth = {'Authorization': 'Bearer ' + os.getenv('YELP_KEY')}
    url = 'https://api.yelp.com/v3/businesses/search?location='

    try:
        # Request from Yelp Fusion API
        url += location
        res = requests.get(url, headers=auth)
        parsed = json.loads(res)
    except json.JSONDecodeError:
        raise Http404
    
    return parsed


def save_to_db(data={}):
    if data == {}:
        raise ValueError('Cannot save nothing to database')
    
    restaurant = Restaurant()
    restaurant.name = data['name']
    restaurant.address = data['location']['city']
    restaurant.city = data['location']['address1']

    restaurant.save()