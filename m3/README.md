# Lab 3: Test-Driven Development

## Introduction

This lab practices the skills needed for Test Driven Development. When developing software, it is important to test features as you build them. This helps ensure the functionality of your code and prevents bugs from cascading into other parts of your application. To do this, we will utilize the Test Driven Development (TDD) approach, which is a software development process that relies on the repetition of a short cycle:

- Write a test for an unimplemented feature
- Run all tests and check that the new test fails
- Write the feature
- Run all tests and check that the new test passes
- Refactor the code

The TDD process will be used throughout this lab. The goal for this lab is to help you better understand your code before you even write it. This practice can help you write better code and prevent bugs from occurring in the future.

## Task 1: Fail the Item Tests

- Open the `itemTests.py` file.
- Examine the unimplemented test functions `test_calculate_item_total_price_converts_discount` and `test_calculate_item_total_price_correct`.
- Complete `TODO 1` inside the `test_calculate_item_total_price_converts_discount` function by writing a test that follows all listed requirements in the comments.
- Complete `TODO 2` inside the `test_calculate_item_total_price_correct` function by writing a test that follows all listed requirements in the comments.
- Run the `test.py` file and examine the output reports, which are located in the `reports` folder and are named by the current date and number of times the testing suite has been run today.

## Task 2: Item Class Implementations

- Open the `invoice.py` file.
- Complete `TODO 3` inside the `calculate_item_total_price` method so that it calculates the price of an item based on the quantity, unit price, and discount.
- Run the `test.py` file and examine the latest output reports. Make sure you are now passing all Item tests.

## Task 3: Fail the Invoice Tests

- Open the `invoiceTests.py` file.
- Examine the unimplemented test functions `test_invoice_add_item_appends_item` and `test_invoice_add_item_checks_discounted`.
- Complete `TODO 4` inside the `test_invoice_add_item_appends_item` function by writing a test that follows all listed requirements in the comments.
- Complete `TODO 5` inside the `test_invoice_add_item_checks_discounted` function by writing a test that follows all listed requirements in the comments.
- Run the `test.py` file and examine the latest output reports. You should be failing the Invoice tests.

## Task 4: Invoice Class Implementations

- Open the `invoice.py` file.
- Complete `TODO 6` inside the `add_item` method so that it appends an item to the invoice.
- Run the `test.py` file and examine the latest output reports. Make sure you are now passing all Invoice tests.

## Submission Details

- On Canvas, submit the following:
  - The URL to your GitHub repository.
  - Make sure that the TAs have been included as collaborators on your repository.
