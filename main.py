import requests
from bs4 import BeautifulSoup

url='https://books.toscrape.com/'
response= requests.get(url)
html=response.text

soup= BeautifulSoup(html, 'html.parser')

#Нахожу все названия книг

title= soup.find_all('img', class_='thumbnail')

lst_title=[]

for ind, ttl in enumerate(title):
    book_title= ttl.get('alt')
    lst_title.append(book_title)





#Нахожу все цены книг
    
price= soup.find_all('p', class_='price_color')

lst_price=[]


for ind, prc in enumerate(price):
    book_price= prc.text
    lst_price.append(book_price[1::])


#Нахожу все ссылки картинок


image= soup.find_all('img', class_='thumbnail')

lst_image=[]


for ind, img in enumerate(image):
    url_img= url + img.get('src')
    lst_image.append(url_img)




inp=int(input('''Какую книгу желаете приобрести? 
1) A Light in the ... 
2) Tipping the Velvet 
3) Soumission 
4) Sharp Objects 
5) Sapiens: A Brief History ... 
6) The Requiem Red 
7) The Dirty Little Secrets ... 
8) The Coming Woman: A ... 
9) The Boys in the ... 
10) The Black Maria 
11) Starving Hearts (Triangular Trade ... 
12) Shakespeare's Sonnets 
13) Set Me Free 
14) Scott Pilgrim's Precious Little ... 
15) Rip it Up and ... 
16) Our Band Could Be ... 
17) Olio 
18) Mesaerion: The Best Science ... 
19) Libertarianism for Beginners 
20) It's Only the Himalayas
Напиши номер книги: '''))



#Нахожу все описания книг

lst_b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

if inp in lst_b:
    url2=url+f'/catalogue/{"-".join(lst_title[inp-1].split(" ")).lower()}_{1000-inp+1}/index.html'
    new_url=url2.replace("'", "")
else:
    print("Вы вышли за пределы. Введите число от 1-20")
    exit()



response2= requests.get(new_url)
html2=response2.text

soup2= BeautifulSoup(html2, 'html.parser')
product_page= soup2.find('p', class_="")


#Ввывод

print(f'''  Название: {lst_title[inp-1]}
    Описание: {product_page.text}
    Цена: {lst_price[inp-1]}
    Картинка: {lst_image[inp-1]}''')
