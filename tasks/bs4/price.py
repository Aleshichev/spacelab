from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep

XPATH = '/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]'

def price_hdd(driver):
    price_hdd = driver.find_element(By.XPATH, f'{XPATH}/div[1]/h4[1]' ).text.replace("$", "")
    return price_hdd

def enter_data(driver, number):
    enter_date = driver.find_element(By.XPATH, f'{XPATH}/div[2]/button[{number}]')
    return enter_date.click()


def find_price(link):
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(f"https://www.webscraper.io{link}")
    sleep(1)
    number = 2
    enter_data(driver, number)
    sleep(1)
    driver.current_url
    price_hdd_256 = price_hdd(driver)
    number += 1
    enter_data(driver, number)
    sleep(1)
    price_hdd_512 = price_hdd(driver)

    driver.quit()
    
    return price_hdd_256, price_hdd_512