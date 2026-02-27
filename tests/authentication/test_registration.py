import pytest
import allure

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

from allure_commons.types import Severity
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpics
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTags.REGISTRATION, AllureTags.REGISTRATION)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStories.REGISTRATION)   # Теперь используем фикстуру
@allure.severity(Severity.CRITICAL)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.sub_suite(AllureStories.REGISTRATION)
class TestRegistration:
    @allure.title('Регистрация пользователя с корректным email, username и password')
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user@gmail.com', username='username', password='password')
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()


# def test_successful_registration(chromium_page: Page):  # Теперь используем фикстуру
#         chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
#
#         email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
#         email_input.fill('user@gmail.com')
#
#         username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
#         username_input.fill('username')
#
#         password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
#         password_input.fill('password')
#
#         registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
#         registration_button.click()
#
#         dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
#         expect(dashboard_title).to_be_visible()