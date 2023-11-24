from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/sivateja/PycharmProjects/pythonProject/Driver/chromedriver.exe"
ser_obj = Service(chrome_driver_path)

driver = webdriver.Chrome(service=ser_obj)
driver.get('https://www.google.com/')

search_box = driver.find_element(By.NAME,'q')  # The name of the search input field
search_box.send_keys("Selenium WebDriver" + Keys.RETURN)

driver.maximize_window()