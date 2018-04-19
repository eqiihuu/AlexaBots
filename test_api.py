# --------------------------------- GOOGLE ---------------------------------- #
from googleplaces import GooglePlaces, types

GOOGLE_KEY = 'AIzaSyA3MjrJS2k3co8PjJvZD9cJzWJogYj_1AA'

google_places = GooglePlaces(GOOGLE_KEY)

# Options: text_search or nearby_search
query_result = google_places.nearby_search(
        location='London, England', keyword='Fish and Chips',
        radius=20000, types=[types.TYPE_FOOD])

if query_result.has_attributions:
    print query_result.html_attributions
# No attributions here

places = list(query_result.places)
for place in places[0:1]:
    # # Returned places from a query are place summaries.
    # print place.name
    # print place.geo_location
    # print place.place_id
    place.get_details()
    # print place.details

    # ---------------- GOOGLE Detailed Information ----------------- #
    # rating
    # utc_offset
    # name
    # reference
    # photos
    # geometry
    # adr_address
    # place_id
    # international_phone_number
    # vicinity
    # reviews
    # formatted_phone_number
    # scope
    # url
    # opening_hours
    # address_components
    # formatted_address
    # id
    # types
    # icon
    # -------------------------------------------------- #
# --------------------------------- YELP ---------------------------------- #
from urllib import quote
import requests

YELP_KEY = '3WSAdduS5EE1g9QSc7t96ve024MhJ4dFthX_7jmBc_qDaE7D6NDcIQb5XdIA5_JKpIK-8evZ8AsmyVqkneNSGm0vpMSxSbP8lBZ5aiKHHmQl62i9MFZPBGxgY0jYWnYx'

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print('Querying {0} ...'.format(url))


    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(api_key, term, location, search_limit=1):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': search_limit
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.

    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)


places = search(YELP_KEY, 'dinner', 'San Francisco, CA')
# print places['businesses'][0].keys()

    # ---------------- YELP Detailed Information ----------------- #
    # region
    #   center
    #       latitude
    #       longitude
    # total
    # businesses: (a list)
    #   rating
    #   review_count
    #   name
    #   transactions
    #   url
    #   price
    #   distance
    #   coordinates
    #   alias
    #   image_url
    #   categories
    #   display_phone
    #   phone
    #   id
    #   is_closed
    #   location
    # -------------------------------------------------- #
