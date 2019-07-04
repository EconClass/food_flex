import requests, json, os
from django.http import Http404
from restaurants.models import Restaurant


# Yelp authorization headers
AUTH = {'Authorization': 'Bearer ' + os.getenv('YELP_KEY')}


def call_api_with_location(location="San Francisco", restaurant="restaurants"):
    """This function searches for restaurants from Yelp's Fusion API
    based on a provided location. It returns a JSON response converted
    into a Python dictionary"""
    
    url = f'https://api.yelp.com/v3/businesses/search?location={location}&term={restaurant}'

    try:
        # Request from Yelp Fusion API
        res = requests.get(url, headers=AUTH)
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
    restaurant.name = data['url']
    restaurant.state = data['location']['state']

    restaurant.save()


def save_10(restaurants=[]):
    """This function saves the first 10 elements in an array of a JSON response"""
    if len(restaurants) <= 0:
        raise ValueError('Cannot save empty data')

    if len(restaurants) > 10:
        restaurants[:10]
    
    for restaurant in restaurants:
        save_to_db(restaurant)
