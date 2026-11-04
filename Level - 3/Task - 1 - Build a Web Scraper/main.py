import requests
from bs4 import BeautifulSoup



url = "https://books.toscrape.com/"



soup = BeautifulSoup(requests.get(url).text, "html.parser")

response = requests.get(url)

print(response.status_code)
print(response.text)