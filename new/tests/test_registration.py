import time

import pytest

from data.data.registration_data import RegistrationData
from data.generator.registartion_generator import RegistrationGenerator
from data.urls import Urls
from pages.registration_page import RegistrationPage


class TestRegistration:
    url = Urls()
    registration_generator = RegistrationGenerator()
    registration_data = RegistrationData()


    def test_registration(self, driver):
        info = next(self.registration_generator.generate_registration_data())
        page = RegistrationPage(driver, self.url.reg_url)
        page.open()
        page.fill_form(info)
        success_message = page.get_success_message()
        assert success_message == self.registration_data.success_reg_message

    @pytest.mark.parametrize("value", [("", "Заполните поле корректно"),
                                       ("hello", "Заполните поле корректно")])
    def test_registration_with_invalid_email(self, driver, value):
        info = next(self.registration_generator.generate_registration_data(email=value[0]))
        page = RegistrationPage(driver, self.url.reg_url)
        page.open()
        page.fill_form(info)
        text = page.get_error_message()
        assert text == value[1]
