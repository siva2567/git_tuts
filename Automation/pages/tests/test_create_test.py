import pytest
from pages.create_page import CreatePage
from utils.webdriver_utils import get_driver
from utils.test_data import TestData

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def create_page(driver):
    return CreatePage(driver)

class TestCreateOperations:
    def test_TC_001_create_product_with_valid_data(self, create_page):
        create_page.open_url(TestData.NOPCOMMERCE_URL)
        create_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        create_page.click_button()
        create_page.navigate_to_catalog()
        create_page.navigate_to_products()
        create_page.click_add_new()
        create_page.fill_product_details(TestData.VALID_PRODUCT_DATA)
        create_page.click_save()
        assert create_page.verify_product_created()

    def test_TC_002_attempt_create_with_invalid_data(self, create_page):
        create_page.open_url(TestData.NOPCOMMERCE_URL)
        create_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        create_page.click_button()
        create_page.navigate_to_catalog()
        create_page.navigate_to_products()
        create_page.click_add_new()
        create_page.fill_product_details(TestData.INVALID_PRODUCT_DATA)
        create_page.click_save()
        assert 'Please enter a valid product name' in create_page.verify_error_message()

   