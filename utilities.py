import datetime
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Utilities:
    """Class Utilities with different useful methods."""
    global SCREENSHOT_DIR
    SCREENSHOT_DIR = "/home/vadim//WebDriver_screenshots/"
    global klika_qa
    klika_qa = "http://qa-test.klika-tech.com/"

    def _set_up(self):
        chromedriver = "/home/vadim/chromedriver/chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get(klika_qa)
        time.sleep(3)

    def _tear_down(self):
        time.sleep(3)
        self.driver.quit()

    def click_specified_buttons(self, buttons=[], *args):
        for item in buttons:
            self.button_click(item)

    def get_values(self):
        field = self.driver.find_element_by_id("display")
        time.sleep(1)
        return field.text

    def make_screenshot(self):
        """A method for making a screenshot of the screen."""
        filename = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.driver.get_screenshot_as_file(SCREENSHOT_DIR + filename + ".png")

    def button_click(self, button):
        try:
            digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
            operations = ["C", "AC", "x", "/", "+", "-", "="]
            if button in digits:
                self.find_elements('digits', button)
            elif button in operations:
                self.find_elements('operations', button)
        except (NoSuchElementException):
            print "Element is not found!"

    def find_elements(self, class_name, li_text):
        html_list = self.driver.find_element_by_class_name(class_name)
        elements = html_list.find_elements_by_tag_name("li")
        for item in elements:
            text = item.text
            if text == li_text:
                item.click()