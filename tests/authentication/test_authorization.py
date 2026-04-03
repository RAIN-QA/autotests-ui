import pytest
import allure

from fixtures.pages import login_page
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage  # Импортируем LoginPage
from pages.authentication.registration_page import RegistrationPage

from allure_commons.types import Severity
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpics
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures
from tools.routes import AppRoute
from config import settings


@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.authorization  # Добавили маркировку authorization
@allure.tag(AllureTags.REGISTRATION, AllureTags.AUTHORIZATION)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStories.AUTHORIZATION)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.sub_suite(AllureStories.AUTHORIZATION)
class TestAuthorization:
    @allure.tag(AllureTags.USER_LOGIN)
    @allure.title("Проверка авторизации с успешной регистрацией")
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(self, registration_page: RegistrationPage, dashboard_page: DashboardPage, login_page: LoginPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.registration_form.check_visible(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()



    @pytest.mark.parametrize('email, password', [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
    ])
    @allure.tag(AllureTags.USER_LOGIN)
    @allure.title("Проверка авторизации с неправильными данными")
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        # Заполняем форму авторизации
        login_page.login_form.fill(email=email, password=password)
        # Нажимаем кнопку "Login"
        login_page.click_login_button()
        # Проверяем наличие сообщения об ошибке
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.tag(AllureTags.NAVIGATION)
    @allure.title("Проверка перехода с авторизации на регистрацию")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration_page(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")