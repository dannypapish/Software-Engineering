# Lab 4: Building a Flask Web Server

## Introduction

In this lab, we will be using [Flask](https://flask.palletsprojects.com/en/2.0.x/) to build a web server. Flask is a micro-web-framework written in Python. We will use it to build a simple web server that can serve dynamic content. This lab is meant to be a gentle introduction to the server-client model and to HTML and CSS. All of the code required from you is in the `app.py` file, but you should read through the html files in the `templates` folder to understand what is going on. Before you begin, make sure you have installed the necessary packages by running a standard `pip install -r requirements.txt` command. If you are still unsure how to do this, refer to the Lab3 README.md file.

## Task 1: Accessing Form Data

- Open the `app.py` file.
- Complete `TODO 1` by accessing the form data for the `age` field and storing it in a variable called `age`.
- Complete `TODO 2` by updating the `GLOBALS` dictionary with the newly found `name` and `age` values.

## Task 2: More Form Data but with Template Rendering

- Complete `TODO 3` by accessing the user's major, credits, and GPA from the form data.
  - **HINT:** Check the `templates/task1.html` file to see what the form data looks like.
- Complete `TODO 4` by updating the `GLOBALS` dictionary with the newly found `major`, `credits`, and `gpa` values.
- Complete `TODO 5` by rendering the `task2.html` template with the correct values.

## Task 3: Calling Functions with Form Data

- Complete `TODO 6` by getting the user's target GPA from the form data and updating the `GLOBALS` dictionary.
- Complete `TODO 7` by calling the `credits_to_target` function with the correct parameters passed in.
- Complete `TODO 8` by rendering the `task3.html` template with the correct values.

## Submission Details

- On Canvas, submit the following:
  - The URL to your GitHub repository, with the latest version of your code pushed to the `main` branch.
  - Make sure that the TAs have been included as collaborators on your repository.
