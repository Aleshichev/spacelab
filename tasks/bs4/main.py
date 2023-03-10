from price import find_price
import json
from data import generate_data
from soup import get_soup

BASE_HTML = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops" 

number = 0
flag = 1
data = {'laptops': []}
try:
    while flag:
        number += 1
        print(number)
        page = f"?page={number}"

        link_html = BASE_HTML+page
        soup = get_soup(link_html)
        titles = soup.find_all(name="a", class_="title")
        flag = titles[0]
        for article_tag in titles:
            link = article_tag.get("href")
            link_html = f"https://www.webscraper.io{link}"
            soup = get_soup(link_html)
            title = soup.find('div', class_='caption').find_next('h4', class_=[]).get_text(strip=True)
            descriptions = soup.find(name="p", class_="description").text.split(",")
            price_hdd_128 = soup.find(name="h4", class_="pull-right price").text.replace("$", "")
           
            price_hdd_256, price_hdd_512 = find_price(link)

            dict_data = generate_data(title, descriptions, price_hdd_128, 
                                  price_hdd_256, price_hdd_512)
            
            data['laptops'].append(dict_data)        


except IndexError:
    print("Страницы закончились")

finally:

    data = json.dumps(data)
    data = json.loads(str(data))

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent = 4)
   
    print("конец программы")

           
