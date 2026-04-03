import pytest
import allure

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

from allure_commons.types import Severity
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpics
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures
from tools.routes import AppRoute
from config import settings


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
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
