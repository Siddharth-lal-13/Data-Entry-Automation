from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from time import sleep

GOOGLE_FORM = "https://forms.gle/AqtsU5tjYoYHYYUm7"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

# Scraping the zillow website
response = requests.get(url=ZILLOW_URL)
web_page_data = response.text

soup = BeautifulSoup(web_page_data, "html.parser")

property_link_list = []
property_address_list = []
property_price_list = []

property_links = soup.find_all(name="a", class_="property-card-link")
for link in property_links:
    property_link_list.append(link.get("href"))

property_addresses = soup.find_all(name="address")
for address in property_addresses:
    property_address_list.append(address.getText().strip("\n ").replace("|", ""))

property_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
for price in property_prices:
    property_price_list.append(price.getText().split("+")[0].strip("/mo"))


# Updating the Google Form
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORM)

for i in range(len(property_address_list)):
    sleep(4)

    input_address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                        '2]/div/div[1]/div/div[1]/input')
    input_address.send_keys(property_address_list[i])

    input_price = driver.find_element(By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                            '1]/div/div[1]/input')
    input_price.send_keys(property_price_list[i])

    input_link = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                           '1]/div/div[1]/input')
    input_link.send_keys(property_link_list[i])

    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    sleep(3)
    more_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    more_response.click()

driver.quit()
