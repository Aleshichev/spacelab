from bs4 import BeautifulSoup
import requests
from log import logger


def get_soup(link_html):
        logger.info(f'Enter in the get_soup() with link_html')

        try:
                response = requests.get(link_html)
                logger.info(f'response {response.status_code}')
                html_page_text = response.text
                soup = BeautifulSoup(html_page_text, "html.parser")
                logger.info(f'return soup')
                return soup
        except Exception as e:
                logger.error(f"Connection Error {e}")
                exit()