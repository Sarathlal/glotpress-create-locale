from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import Config
 
driver = webdriver.Firefox()

#launch URL
url = Config.SITE_URL
driver.get(url)

#identify search box
m = driver.find_element(by=By.NAME, value="q")

#enter search text
m.send_keys("Open Source")

#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)