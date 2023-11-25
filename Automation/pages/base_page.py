class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element_to_be_visible(self, by_locator, timeout=10):
    
            
        
        pass

    def wait_for_element_to_be_clickable(self, by_locator, timeout=10):
        # Implement the wait logic for element clickability
        pass

    def click_element(self, by_locator):
        self.wait_for_element_to_be_clickable(by_locator)
        self.driver.find_element(*by_locator).click()

    def send_keys_to_element(self, by_locator, keys):
        self.wait_for_element_to_be_visible(by_locator)
        self.driver.find_element(*by_locator).send_keys(keys)

    def get_text_of_element(self, by_locator):
        self.wait_for_element_to_be_visible(by_locator)
        return self.driver.find_element(*by_locator).text

    def get_attribute_of_element(self, by_locator, attribute):
        self.wait_for_element_to_be_visible(by_locator)
        return self.driver.find_element(*by_locator).get_attribute(attribute)
