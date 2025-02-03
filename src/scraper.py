import requests
from bs4 import BeautifulSoup
from config import HEADERS  # Ensure HEADERS is properly loaded

def fetch_amazon_page(url):
    """Fetch Amazon search page and return BeautifulSoup object"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raises an error if response status is not 200
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    return None
