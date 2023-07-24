from utils import get_chromedriver_path, create_driver
import time


def chrome_test(path_to_chromedriver):
    # Requires the chromedriver executable to be in the chromedriver folder of this lab
    driver = create_driver(path_to_chromedriver)

    # URL from Postman Step
    driver.get('https://www.indeed.com/jobs?q=Software+Engineer&l=Charlotte')
    print(driver.page_source)

    time.sleep(5)  # Time delay so the page can be seen for longer
    driver.quit()  # Always remember to quit the driver


def main():
    chrome_test(get_chromedriver_path())


if __name__ == '__main__':
    main()
