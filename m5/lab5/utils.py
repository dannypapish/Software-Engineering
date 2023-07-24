from selenium import webdriver
import os

ROUTES = ["fiction_10", "science_22", "poetry_23", "parenting_28", "humor_30",
          "food-and-drink_33", "thriller_37", "novels_46", "health_47"]


def get_chromedriver_path():
    """Returns the path to the chromedriver executable"""
    return os.path.join(os.getcwd(), 'chromedriver/chromedriver')


def create_driver(path_to_chromedriver: str) -> webdriver.Chrome:
    """Creates a driver object"""
    return webdriver.Chrome(path_to_chromedriver)


def build_books_to_scrape_url(route: str) -> str:
    """Returns the URL to the books to scrape website for the scraping scavenger hunt"""
    base_url = "http://books.toscrape.com/catalogue/category/books/"
    return os.path.join(base_url, route, "index.html")


def sort_dict_by_value(dictionary: dict) -> list:
    """Returns a list of tuples sorted by the value of the dictionary"""
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)


def write_titles_to_file(filename: str, book_titles: list):
    """Writes a list of book titles to the file"""
    with open(os.path.join(os.getcwd(), filename), 'a') as file:
        for title in book_titles:
            file.write(title + "\n")


def erase_file(filename: str):
    """Erases a file"""
    with open(os.path.join(os.getcwd(), filename), 'w') as file:
        file.write('')


def write_smallest_and_largest_books(filename: str, categories: list):
    """Writes the smallest and largest book categories to the file"""
    with open(os.path.join(os.getcwd(), filename), 'a') as file:
        file.write("Largest Category: " +
                   categories[0][0] + " with " + str(categories[0][1]) + " books\n")
        file.write("Smallest Category: " +
                   categories[-1][0] + " with " + str(categories[-1][1]) + " books\n")

def write_lines_to_html_list(filename: str, text: list):
    """Writes a list of lines to an html list"""
    with open(os.path.join(os.getcwd(), filename), 'a') as file:
        file.write("<ul>\n")
        for line in text:
            file.write("<li>" + line + "</li>\n")
        file.write("</ul>\n")

def check_html_content_length(filename: str) -> bool:
    """Returns True if the html file has any lines other than the default header"""
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        return (len(file.readlines()) != 1)
    
def write_html_header(filename: str):
    """Writes the html header to the file"""
    with open(os.path.join(os.getcwd(), filename), 'a') as file:
        file.write("<h1>Scraping Books</h1>\n")



