from bs4 import BeautifulSoup
import requests

URL = 'https://www.profit.ro/toate'
provider = 'profit.ro'
entries = []



response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
featured = soup.find(class_='feature')
featuredAnchor = featured.find('a', href=True)
featuredUrl = provider + featuredAnchor['href']
featuredText = featuredAnchor.get('title')
print(featuredUrl)
print(featuredText)

featuredEntry = {
    'title': featuredText,
    'url': featuredUrl,
    'provider': provider
}