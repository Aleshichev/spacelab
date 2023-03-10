from bs4 import BeautifulSoup
import requests
from price import find_price
import json


BASE_HTML = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops" 

number = 2
flag = 1

try:
    while flag:
        number += 1
        page = f"?page={number}"
        print(page)
        response = requests.get(BASE_HTML+page)
        html_page_text = response.text
        soup = BeautifulSoup(html_page_text, "html.parser")
        titles = soup.find_all(name="a", class_="title")
        flag = titles[0]
        for article_tag in titles:
            list_data = []
            dict_data = {}
            title = article_tag.getText()
            link = article_tag.get("href")
            list_data.append(title)            
            # print(title)
            response_deeper = requests.get(f"https://www.webscraper.io{link}")
            html_deep_page_text = response_deeper.text
            soup_deep = BeautifulSoup(html_deep_page_text, "html.parser") 
            descriptions = soup_deep.find(name="p", class_="description").text.replace(" ", "").split(",")
            price_hdd_128 = soup_deep.find(name="h4", class_="pull-right price").text
            # print(descriptions)
            # print(price_hdd_128)
            list_data.append(descriptions)
            list_data.append(price_hdd_128)
            price_hdd_256, price_hdd_512 = find_price(link)
            list_data.append(price_hdd_256)
            list_data.append(price_hdd_512)
            dict_data = {'title': title,
                         'descriptions': {'monitor': descriptions[0],
                                          'processor': descriptions[1],
                                          'RAM': descriptions[2],
                                          'HDD': descriptions[3],
                                          'OS': descriptions[4]
                                          },
                         'price_hdd_128': price_hdd_128,
                         'price_hdd_256': price_hdd_256,
                         'price_hdd_512': price_hdd_512}
            print(dict_data)
            print(type(dict_data))
            jsonStr = json.dumps(dict_data)
            print(jsonStr)
            print(type(jsonStr))
            # print(list_data)
            

except IndexError:
    print("Страницы закончились")
finally:
    print("конец программы")

           
