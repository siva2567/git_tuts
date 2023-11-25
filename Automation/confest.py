import pytest
from utils.webdriver_utils import get_driver

@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
