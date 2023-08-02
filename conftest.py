import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://automation.credence.in")
    driver.maximize_window()
    return driver

@pytest.fixture(params=[
    ("CredTeam123@test.com", "cred123"),  # valid username and password
    ("CredTeam12@test.com", "cred123"),   # invalid username and valid password
    ("CredTeam123@test.com", "cred12"),   # valid username and invalid password
    ("CredTeam12@test.com", "cred12")     # invalid username and invalid password
    ])

def getDataforlogin(request):
    return request.param