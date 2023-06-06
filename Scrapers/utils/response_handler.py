from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import logging
import urllib.parse
import requests

dynamic_content_sites = ['www.g4media.ro']

def parse_response(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError(f"Invalid URL: {url}")

        needs_dynamic_content = False
        if parsed_url.netloc in dynamic_content_sites:
            needs_dynamic_content = True

        if needs_dynamic_content:
            options = Options()
            options.add_argument("--headless")  
            driver = webdriver.Chrome(options=options) 
            driver.get(url)
            page_source = driver.page_source
            driver.quit()
        else:
            headers = {'User-Agent': 'Mozilla/5.0'}
            with requests.get(url, headers=headers) as response:
                response.raise_for_status()
                page_source = response.text

        soup = BeautifulSoup(page_source, 'html.parser')
        if soup is None:
            raise ValueError("Failed to parse HTML")
        return soup

    except requests.exceptions.RequestException as e:
        logging.error(f"Error making request: {e}")
        return None
    except ValueError as e:
        logging.error(str(e))
        return None
