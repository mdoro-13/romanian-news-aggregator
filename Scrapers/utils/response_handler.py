import requests
import urllib.parse
from bs4 import BeautifulSoup


def parse_response(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError(f"Invalid URL: {url}")

        headers = {'User-Agent': 'Mozilla/5.0'}
        with requests.get(url, headers=headers) as response:
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            if soup is None:
                raise ValueError("Failed to parse HTML")
            return soup

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error making request: {e}") from e
    except ValueError as e:
        raise ValueError(str(e)) from e
