from django.shortcuts import render
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from django.core.paginator import Paginator

# Create your views here.

def details(request):
    # d = {"name":{"value":"btc", "value3":"eth"}, "price":2345, "num":1234, "invoice":4321, "list":True}
    storedAPI = []

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c812dd07-0bba-4591-ac78-5fefcdbe13e2',
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    API_DATA = response.json()

    paginator = Paginator(API_DATA['data'], 15)  # Display 10 items per page

    # Get the current page number from the query parameters, default to 1
    page_number = request.GET.get('page', 1)

    # Get the page object for the current page number
    page_obj = paginator.get_page(page_number)

    return render(request, "index.html", {"page_obj":page_obj})

def bookmark_toggle(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.user.is_authenticated:
        item.bookmarked = not item.bookmarked  # Toggle bookmark status
        item.save()



