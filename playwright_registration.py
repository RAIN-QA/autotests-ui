from playwright.sync_api import sync_playwright, expect # Импорт Playwright для синхронного режима и проверки

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()   # Создаем новую страницу

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_registration = page.get_by_test_id('registration-form-email-input').locator('input')
    email_registration.fill('user.name@gmail.com')

    username_registration = page.get_by_test_id('registration-form-username-input').locator('input')
    username_registration.fill('username')

    password_registration = page.get_by_test_id('registration-form-password-input').locator('input')
    password_registration.fill('password')

    button_click = page.get_by_test_id('registration-page-registration-button')
    button_click.click()

    dash_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dash_title).to_be_visible()
    expect(dash_title).to_have_text('Dashboard')

