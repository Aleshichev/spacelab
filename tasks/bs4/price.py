from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep

def find_price(link):
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(f"https://www.webscraper.io{link}")
    sleep(1)
    enter_date = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[2]/button[2]')
    enter_date.click()
    sleep(1)
    driver.current_url
    price_hdd_256 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]' ).text
    enter_date = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[2]/button[3]')
    enter_date.click()
    sleep(1)
    price_hdd_512 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]' ).text

    return price_hdd_256, price_hdd_512