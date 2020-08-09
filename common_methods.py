from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class Wait:
    def __init__(self, driver, time=20):
        self.__wait = WebDriverWait(driver, time)
        self.__driver = driver

    def get_by_xpath(self, xpath):
        self.__wait.until(presence_of_element_located((By.XPATH, xpath)))
        return self.__driver.find_element_by_xpath(xpath)

    def get_multiple_by_xpath(self, xpath):
        self.__wait.until(presence_of_element_located((By.XPATH, xpath)))
        return self.__driver.find_elements_by_xpath(xpath)
