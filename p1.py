import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://books.toscrape.com/'

bookheader ={
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'
}

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

books = [book.text for book in soup.find_all('h3')]

pd.DataFrame({'Book Title': books}).to_csv('booksdatas.csv')

print("Book data saved to booksdata.csv")
