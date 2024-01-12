import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    response = requests.get(url)
    return response.text

def parse_html(webpage_text):
    parsed_html = BeautifulSoup(webpage_text, 'html.parser')
    return parsed_html

def extract_data(parsed_html):
    # This is a placeholder implementation. The actual implementation will depend on the data the user wants to extract.
    data = parsed_html.find_all('p')
    return data
