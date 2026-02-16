import pytest
from selenium.webdriver import Firefox, Chrome


@pytest.fixture(scope="session")
def driver():
    yield Firefox()


@pytest.fixture(scope="module")
def base_url(driver):
    driver.get("http://localhost:8000")
    yield driver


@pytest.fixture(scope="module")
def action(driver): 
    driver.get("http://localhost:8000/action.html")
    yield driver
