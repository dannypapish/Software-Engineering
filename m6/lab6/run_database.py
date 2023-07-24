from database_manager import JobsDatabase
from json_writer import dict_list_to_json
from scrape_jobs import *
from utils import get_chromedriver_path


def populate_database(jobs: list) -> JobsDatabase:
    """
    Creates a new database and populates it with the jobs.

    args:
        - jobs: list of jobs

    returns:
        - JobsDatabase object
    """
    jobs_database = None

    # TODO 7: Create a new JobsDatabase object called `jobs_database`
    jobs_database = JobsDatabase()

    # TODO 8: Create the jobs table
    jobs_database.create_table()

    # TODO 9: Clear out all jobs from the database
    # - look through the database_manager.py file to find the correct function for deleting all jobs
    jobs_database.delete_all_jobs()

    # TODO 10: Loop over the jobs and put them in the database
    # - look through the database_manager.py file to find the correct function for inserting a job
    for job in jobs:
        jobs_database.insert_job(job)

    return jobs_database


def pull_and_print_all_from_database(jobs_database: JobsDatabase):
    """
    Pulls all jobs from the database and prints them.

    args:
        - jobs_database: JobsDatabase object
    """
    # TODO 11: Pull all jobs from the database, then loop through and print them
    # - look through the database_manager.py file to find the correct function for getting all jobs
    all_jobs = jobs_database.get_all_jobs()
    for job in all_jobs:
        print(job)


def main():
    chromedriver_path = get_chromedriver_path()
    url = create_scraping_url("Software", "Charlotte")
    jobs = scrape_jobs(chromedriver_path, url)
    jobs_database = populate_database(jobs)
    pull_and_print_all_from_database(jobs_database)
    jobs_database.close()


if __name__ == "__main__":
    main()
