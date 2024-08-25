import pytest
from selenium import webdriver


@pytest.fixture
def Setup():
    driver = webdriver.Chrome()
    driver.get("https://automation.credence.in/login")
    driver.maximize_window()
    return driver
