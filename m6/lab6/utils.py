from selenium import webdriver
import os

ROLES = ['Software Engineer', 'Data Scientist', 'Data Engineer']
LOCATIONS = ['Charlotte', 'New York', 'San Diego']


def get_chromedriver_path():
    """Returns the path to the chromedriver executable"""
    return os.path.join(os.getcwd(), 'chromedriver/chromedriver')


def create_driver(path_to_chromedriver: str = get_chromedriver_path()) -> webdriver.Chrome:
    """Creates a driver object"""
    return webdriver.Chrome(path_to_chromedriver)


def erase_file(filename):
    """
    Erases the contents of a file.
    - filename: name of the file to erase
    """
    with open(filename, "w") as file:
        file.write("")
