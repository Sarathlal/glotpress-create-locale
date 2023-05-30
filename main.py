import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from config import Config
 
driver = webdriver.Firefox()

# Login to WordPress
def login():
    driver.get(Config.LOGIN_URL)

    # Target the user name field
    user_name_field = driver.find_element(by=By.ID, value="user_login")

    # Fill the user name
    user_name_field.send_keys(Config.USER_NAME)

    # Target the password field
    password_field = driver.find_element(by=By.ID, value="user_pass")

    #Fill the password field
    password_field.send_keys(Config.PASSWORD)

    driver.find_element(by=By.ID, value="loginform").submit()

def visit_frontend():
    driver.get(Config.SITE_URL)

# Iterate throgh locale file
def iterate_locale():
    # Open file 
    with open(Config.LOCALE_LIST) as file_obj:
        
        # Create reader object by passing the file object
        reader_obj = csv.reader(file_obj)
        
        # Iterate over each row in the csv file
        for row in reader_obj:
            time.sleep(2)
            create_locale(row[0], row[1])

# Create locale
def create_locale(locale_code, locale_name):

    create_locale_url = Config.GLOTPRESS_URL + '/sets/-new/?project_id=' + str(Config.GLOTPRESS_PROJECT_ID)
    driver.get(create_locale_url)
 
    # Scroll to top
    driver.execute_script("window.scrollTo(0, 0)")

    time.sleep(1)

    sel = Select(WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "set[locale]"))
    ))
    sel.select_by_value(locale_code)

    time.sleep(1)

    # Target the locale name field
    locale_name_field = driver.find_element(by=By.ID, value="set[name]")
    # Fill the locale name
    locale_name_field.send_keys(locale_name)

    time.sleep(1)

    # Target the submit button
    form = driver.find_element(by=By.CLASS_NAME, value="gp-content").find_element(by=By.TAG_NAME, value="form").submit()


login()
time.sleep(1)
iterate_locale()