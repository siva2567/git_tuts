from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CreatePage(BasePage):
    button=(By.XPATH,'//*[@id="nopSideBarPusher"]/i')
    catalog=(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a/p/i")
    ADD_NEW_BUTTON = (By.XPATH, "/html/body/div[3]/div[1]/form[1]/div/div/a")
    PRODUCT_NAME_INPUT = (By.ID, "Name")
    DESCRIPTION_INPUT = (By.ID, "ShortDescription")
    SAVE_BUTTON = (By.ID, '//*[@id="product-form"]/div[1]/div/button[1]')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="product-form"]/div[2]/ul/li')
    PRODUCT_CREATED_MESSAGE = (By.XPATH, "/html/body/div[3]/div[1]/div[1]")

    def navigate_to_products(self):
        # Assuming there is a "Products" link or button that takes you to the product page
        products_link = (By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a")
        self.click_element(products_link)

    def verify_product_created(self):
        product_created_message = self.get_text_of_element(self.PRODUCT_CREATED_MESSAGE)
        # Assuming there is a success message displayed after successful product creation
        return "The new product has been added successfully" in product_created_message
