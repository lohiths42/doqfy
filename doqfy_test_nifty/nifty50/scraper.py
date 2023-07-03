import redis
from nifty50.models import Nifty50Data
from datetime import datetime
from bs4 import BeautifulSoup
import requests

def scrape_and_store_data():
    # Scrape data from the URL
    url = "https://www.nseindia.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract the relevant data from the table
    # Update this code according to the structure of the Nifty 50 table on the website
    # You may need to inspect the HTML structure of the table and adapt the code accordingly
    data_table = soup.find("table", {"class": "nifty50_table"})
    rows = data_table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        timestamp = datetime.now()
        value = float(cells[0].text.strip())
        
        # Store the data in Redis
        redis_client = redis.Redis(host='localhost', port=6379, db=0)
        redis_client.set(timestamp, value)
        
        # Save the data in the Django model as well
        nifty50_data = Nifty50Data(timestamp=timestamp, value=value)
        nifty50_data.save()
