from bs4 import BeautifulSoup
import requests
for i in range(1,51):
    url=f'http://books.toscrape.com/catalogue/page-{i}.html'
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    books = soup.find_all('article',class_='product_pod')
    for book in books:
        title = book.h3.a.attrs['title']
        print(title)
        price = book.find('div',class_='product_price').p
        print(price.text)
        img_src = book.img.attrs['src']
        img_url= f'http://books.toscrape.com{img_src}'
        print(img_url)
        print()

