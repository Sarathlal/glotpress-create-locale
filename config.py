import os
from dotenv import load_dotenv
load_dotenv()

# # Set the working directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Find the absolute file path to the top level project directory
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Base configuration class. Contains default configuration settings + configuration settings applicable to all environments.
    """
    #GlotPress params
    GLOTPRESS_URL_BASE = 'portal'
    GLOTPRESS_PROJECT_ID = 1

    # URLs
    SITE_URL = os.getenv('SITE_URL', default='')
    LOGIN_URL = os.getenv('SITE_URL') + '/wp-login.php'
    GLOTPRESS_URL = SITE_URL + GLOTPRESS_URL_BASE


    # Credentails
    USER_NAME = os.getenv('USER_NAME')
    PASSWORD = os.getenv('PASSWORD')

    # WP locale CSV file
    LOCALE_LIST = basedir + '/wp-locale.csv'