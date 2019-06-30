import requests, json, os
from django.http import Http404
from .models import Restaurant


def call_api_with_key(location="San Francisco"):
    """This function searches for restaurants from Yelp's Fusion API
    based on a provided location. It returns a JSON response converted
    into a Python dictionary"""

    # Yelp authorization headers
    auth = {'Authorization': 'Bearer ' + os.getenv('YELP_KEY')}
    url = 'https://api.yelp.com/v3/businesses/search?term=restaurants&location='

    try:
        # Request from Yelp Fusion API
        url += location
        res = requests.get(url, headers=auth)
        parsed = json.loads(res)
    except json.JSONDecodeError:
        raise Http404
    
    return parsed


def save_to_db(data={}):
    """This function saves parsed JSON data (Python dictionaries) to the database"""
    if data == {}:
        raise ValueError('Cannot save nothing to database')
    
    restaurant = Restaurant()
    restaurant.name = data['name']
    restaurant.address = data['location']['city']
    restaurant.city = data['location']['address1']

    restaurant.save()


def save_10(restaurants=[]):
    """This function saves the first 10 elements in an array of a JSON response"""
    if len(restaurants) <= 0:
        raise ValueError('Cannot save empty data')

    if len(restaurants) > 10:
        restaurants[:10]
    
    for restaurant in restaurants:
        save_to_db(restaurant)

if __name__ == "__main__":
    parsed = call_api_with_key()
    save_10(parsed['businesses'])