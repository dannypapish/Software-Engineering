from scrape_jobs import *
from json import dumps
from utils import erase_file, get_chromedriver_path, LOCATIONS, ROLES


def dict_list_to_json(dict_list, filename):
    """
    Writes a list of dictionaries to a json file
    - dict_list: list of dictionaries
    - filename: name of the file to write to
    """
    with open(filename, "a") as file:
        # TODO 6: Use the correct function to write the list of dictionaries to a json file
        # - set the indent to 4 for the json string
    
        json_data = dumps(dict_list, indent=4)  
        file.write(json_data)



def test_json_writer():
    """
    Tests the json writer.
    """
    erase_file("jobs.json")
    chromedriver_path = get_chromedriver_path()
    full_results = {}
    for location in LOCATIONS:
        full_results[location] = {}
        for role in ROLES:
            url = create_scraping_url(role, location)
            jobs = scrape_jobs(chromedriver_path, url)
            full_results[location][role] = jobs
    dict_list_to_json(full_results, "jobs.json")
    #print(full_results)


if __name__ == "__main__":
    test_json_writer()
