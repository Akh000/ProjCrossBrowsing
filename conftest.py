import pytest
from selenium import webdriver

# add arg --broswer this for your command linner
def pytest_addoption(parser):
    parser.addoption("--browser")

#passing the value to --browser
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Define the browser fixture function with a single argument, request.
# Within the browser function, use the request.config.getoption() method to get the value
# of the --browser option passed to pytest on the command line.


# here we are passing actual value to --browser
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        print("Default Browser Open")
    driver.maximize_window()
    driver.get("https://automation.credence.in/login")
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")