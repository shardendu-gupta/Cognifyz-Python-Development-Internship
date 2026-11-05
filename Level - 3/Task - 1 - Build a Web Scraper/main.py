import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)
print("Status Code:", response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

book_data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()
    rating = book.find("p", class_="star-rating")["class"][1]
    book_data.append([title, price, availability, rating])

    print("Title:", title)
    print("Price:", price)
    print("Availability:", availability)
    print("Rating:", rating)
    print("------------------------")


with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability", "Rating"])
    writer.writerows(book_data)

print("Total Books:", len(book_data))
print("Data saved successfully!")
