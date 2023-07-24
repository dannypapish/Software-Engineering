import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class JobsDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("jobs.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,
                image_url TEXT
            )
            """
        )
        self.connection.commit()

    def insert_job(self, job):
        self.cursor.execute(
            """
            INSERT INTO jobs (title, company, image_url)
            VALUES (?, ?, ?)
            """,
            (job["title"], job["company"], job["image_url"])
        )
        self.connection.commit()

    def get_all_jobs(self):
        self.cursor.execute(
            """
            SELECT * FROM jobs
            """
        )
        return self.cursor.fetchall()

    def delete_all_jobs(self):
        self.cursor.execute(
            """
            DELETE FROM jobs
            """
        )
        self.connection.commit()

    def get_job_by_id(self, job_id):
        self.cursor.execute(
            """
            SELECT * FROM jobs WHERE id = ?
            """,
            (job_id,)
        )
        return self.cursor.fetchone()

    def delete_job_by_id(self, job_id):
        self.cursor.execute(
            """
            DELETE FROM jobs WHERE id = ?
            """,
            (job_id,)
        )
        self.connection.commit()

    def update_job_by_id(self, job_id, job):
        self.cursor.execute(
            """
            UPDATE jobs SET title = ?, company = ?, image_url = ? WHERE id = ?
            """,
            (job["title"], job["company"], job["image_url"], job_id)
        )
        self.connection.commit()

    def get_jobs_by_company(self, company):
        self.cursor.execute(
            """
            SELECT * FROM jobs WHERE company = ?
            """,
            (company,)
        )
        return self.cursor.fetchall()

    def get_jobs_by_phrase_in_title(self, title):
        self.cursor.execute(
            """
            SELECT * FROM jobs WHERE title LIKE ?
            """,
            (f"%{title}%",)
        )
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
