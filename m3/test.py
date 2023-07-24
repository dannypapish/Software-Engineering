from datetime import datetime
from itemTests import *
from invoiceTests import *
import os

# -------- Testing Function Constants --------

ITEM_FUNCS = [test_item_initializes_name,
              test_item_initializes_quantity,
              test_item_initializes_unit_price,
              test_item_initializes_discount_percent_false,
              test_item_initializes_discount_percent_true,
              test_calculate_item_total_price_converts_discount,
              test_calculate_item_total_price_correct]

INVOICE_FUNCS = [test_invoice_initializes_name,
                 test_invoice_initializes_date,
                 test_invoice_initializes_discounted_false,
                 test_invoice_initializes_discounted_true,
                 test_invoice_add_item_appends_item,
                 test_invoice_add_item_checks_discounted]


TESTING_FUNCTIONS = {"item": ITEM_FUNCS,
                     "invoice": INVOICE_FUNCS}


def run_tests(test_type: str, test_funcs: list, report_file_path: str) -> int:
    """
    Runs all tests for a given set of test functions.

    args:
        - test_funcs: a list of test functions to run.
        - report_file_path: the path to the report file, where the results of the tests will be written.

    returns:
        - the number of failed tests as an integer.

    modifies:
        - Writes the results of the tests to the report file.
    """
    failed_tests = 0
    with open(report_file_path, "a") as report_file:
        for test in test_funcs:
            result, error = test()
            if not result:
                report_file.write(f"{error}\n")
                failed_tests += 1
        report_file.write(f"{test_type} tests complete.\n")
        report_file.write(
            f"{len(test_funcs) - failed_tests} out of {len(test_funcs)} tests passed.\n")


def create_report_folder() -> str:
    """
    Creates a folder for the test reports.

    args:
        - None

    returns:
        - a unique, identifiable folder path for the reports as a string.

    modifies:
        - Creates a folder for the test reports.
    """
    copy_flag = 0
    current_date = datetime.now().strftime("%Y-%m-%d")
    report_folder_path = f"reports/{current_date}_{copy_flag}"
    while os.path.exists(report_folder_path):
        copy_flag += 1
        report_folder_path = f"reports/{current_date}_{copy_flag}"
    os.makedirs(report_folder_path)
    return report_folder_path


def create_report_file(report_folder_path: str, test_type: str) -> str:
    """
    Creates a report file for a given test type.

    args:
        - report_folder_path: the path to the folder where the reports will be stored.
        - test_type: the type of tests being run.

    returns:
        - the path to the report file as a string.
    """
    report_file_path = f"{report_folder_path}/{test_type}_report.txt"
    with open(report_file_path, "w") as report_file:
        report_file.write(f"Test report for {test_type} tests.\n")
    return report_file_path


def main() -> None:
    """
    Runs all tests.
    """
    report_folder_path = create_report_folder()
    for test_type, test_funcs in TESTING_FUNCTIONS.items():
        report_file_path = create_report_file(report_folder_path, test_type)
        run_tests(test_type, test_funcs, report_file_path)


if __name__ == "__main__":
    main()
