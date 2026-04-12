import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

book_list = []


#Need to extract data from all pages
print("Iniciando extração de dados...")
for pagina in range(1,51):

    url = f'https://books.toscrape.com/catalogue/page-{pagina}.html'

    page = requests.get(url)
    page_data = BeautifulSoup(page.text, 'html.parser')

    all_products = page_data.find_all('article', class_="product_pod")

    #extracting data from all books of each page
    for book in all_products:
        title = book.h3.a['title']

        text_price = book.find('p', class_="price_color").text

        availability = book.find('p', class_="instock availability").text.strip()

        rate = book.find('p', class_='star-rating')['class'][1]

        book_list.append({
            'Title': title,
            'Price': text_price,
            'Availability': availability,
            'Rate': rate
        })

    print(f'Pagina {pagina} concluída com sucesso!')

    #wait some time before going to the next page
    #pause = random.uniform(0.3,1)
    time.sleep(0.1)

df = pd.DataFrame(book_list)
print(df.head())
df.to_csv('Books_catalog', index=False, encoding='utf-8')
