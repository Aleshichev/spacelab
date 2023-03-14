from bs4 import BeautifulSoup
import requests
from log import logger

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def get_soup(link_html):
        logger.info(f'Enter in the get_soup() with link_html')

        try:
                response = requests.get(url=link_html, headers=headers)
                logger.info(f'response {response.status_code}')
                html_page_text = response.text
                soup = BeautifulSoup(html_page_text, "html.parser")
                logger.info(f'return soup')
                return soup
        except Exception as e:
                logger.error(f"Connection Error {e}")
                exit()