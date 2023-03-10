from bs4 import BeautifulSoup
import requests

def get_soup(link_html):
        try:
                response = requests.get(link_html)
                html_page_text = response.text
                soup = BeautifulSoup(html_page_text, "html.parser")
                return soup
        except Exception as e:
                print(f"Connection Error {e}")
                exit()