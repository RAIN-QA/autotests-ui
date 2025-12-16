import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage  # Импортируем LoginPage

@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.authorization  # Добавили маркировку authorization
@pytest.mark.parametrize('email, password', [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # Заполняем форму авторизации
    login_page.fill_login_form(email=email, password=password)
    # Нажимаем кнопку "Login"
    login_page.click_login_button()
    # Проверяем наличие сообщения об ошибке
    login_page.check_visible_wrong_email_or_password_alert()

# # Использование фикстуры 'chromium_page', которая автоматически предоставляет готовую страницу
# def test_wrong_email_or_password_authorization1(page: Page, email: str, password: str):
#     # Теперь страница передаётся в тест через фикстуру 'chromium_page', браузер не нужно инициализировать вручную
#
#         page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
#
#         email_input = page.get_by_test_id('login-form-email-input').locator('input')
#         email_input.fill(email)
#
#         password_input = page.get_by_test_id('login-form-password-input').locator('input')
#         password_input.fill(password)
#
#         login_button = page.get_by_test_id('login-page-login-button')
#         login_button.click()
#
#         wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
#         expect(wrong_email_or_password_alert).to_be_visible()
#         expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")