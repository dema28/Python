import time

from locators.alert_page_herokuapp_locators import AlertPageLocators
from pages.base_page import BasePage


class AlertPage(BasePage):

    locators = AlertPageLocators()

    def alert(self):
        self.element_is_clickable(self.locators.ALERT_LOCATOR).click()
        self.alert_is_visible()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def alert_confirm(self, value):
        self.element_is_clickable(self.locators.ALERT_CONFIRM_LOCATOR).click()
        self.alert_is_visible()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        if value == "YES":
            alert.accept()
        else:
            alert.dismiss()
        return alert_text

    def alert_prompt(self, value):
        self.element_is_clickable(self.locators.ALERT_PROMPT_LOCATOR).click()
        self.alert_is_visible()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.send_keys(value)
        alert.accept()
        return alert_text

    def get_text(self):
        text = self.element_is_visible(self.locators.TEXT_LOCATOR).text
        return text
