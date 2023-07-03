from django.shortcuts import render
from nifty50.models import Nifty50Data
import redis

def display_data(request):
    # Retrieve data from Redis
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    data = []
    for key in redis_client.keys():
        value = redis_client.get(key)
        data.append((key.decode(), value.decode()))
    
    # Pass the data to the template for rendering
    context = {'data': data}
    return render(request, 'nifty50/card_layout.html', context)
