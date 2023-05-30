from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import Config
 
driver = webdriver.Firefox()

# #launch URL
# url = Config.SITE_URL
# driver.get(url)

# #identify search box
# m = driver.find_element(by=By.NAME, value="q")

# #enter search text
# m.send_keys("Open Source")

# #perform Google search with Keys.ENTER
# m.send_keys(Keys.ENTER)

def login():
    url = Config.ADMIN_URL
    driver.get(url)

    # Target the user name field
    user_name_field = driver.find_element(by=By.ID, value="user_login")

    # Fill the user name
    user_name_field.send_keys(Config.USER_NAME)

    # Target the password field
    password_field = driver.find_element(by=By.ID, value="user_pass")

    #Fill the password field
    password_field.send_keys(Config.PASSWORD)

    driver.find_element(by=By.ID, value="loginform").submit()



login()