import pytest
from playwright.sync_api import sync_playwright, expect, Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

# @pytest.mark.regression
# @pytest.mark.courses
# def test_empty_courses_list():
#     # Открываем браузер с использованием Playwright
#     with sync_playwright() as playwright:
#         # Запускаем Chromium браузер в обычном режиме (не headless)
#         browser = playwright.chromium.launch(headless=False)
#         # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
#         context = browser.new_context()
#         # Открываем новую страницу в рамках контекста
#         page = context.new_page()
#
#         page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
#
#         email_input = page.get_by_test_id('registration-form-email-input').locator('input')
#         email_input.fill('user.name@gmail.com')
#
#         username_input = page.get_by_test_id('registration-form-username-input').locator('input')
#         username_input.fill('username')
#
#         password_input = page.get_by_test_id('registration-form-password-input').locator('input')
#         password_input.fill('password')
#
#         registration_button = page.get_by_test_id('registration-page-registration-button')
#         registration_button.click()
#
#         # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
#         context.storage_state(path="browser-state.json")
#
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
#         page = context.new_page()
#
#         page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
#
#         course_icon = page.get_by_test_id('courses-list-toolbar-title-text')
#         expect(course_icon).to_be_visible()
#         expect(course_icon).to_have_text('Courses')
#
#         file_icon = page.get_by_test_id('courses-list-empty-view-icon')
#         expect(file_icon).to_be_visible()
#
#         result_text = page.get_by_test_id('courses-list-empty-view-title-text')
#         expect(result_text).to_be_visible()
#         expect(result_text).to_have_text('There is no results')
#
#         load_result_text = page.get_by_test_id('courses-list-empty-view-description-text')
#         expect(load_result_text).to_be_visible()
#         expect(load_result_text).to_have_text('Results from the load test pipeline will be displayed here')


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list2(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.sidebar.click_courses()
    courses_list_page.sidebar.check_visible()
    courses_list_page.navbar.check_visible("username")

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    # Проверен заголовок "Create course"
    create_course_page.check_visible_create_course_title()
    # Проверено, что кнопка создания курса disabled
    create_course_page.check_disabled_create_course_button()
    # Проверен пустой предпросмотр изображения
    create_course_page.check_visible_image_preview_empty_view()
    # Проверен блок загрузки изображения в состоянии без выбранной картинки
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    # Проверена форма со значениями по умолчанию
    create_course_page.check_visible_create_course_form(title="", description="", estimated_time="", max_score="0", min_score="0")
    # Проверен заголовок "Exercises"
    create_course_page.check_visible_exercises_title()
    # Проверена кнопка создания задания
    create_course_page.check_visible_create_exercise_button()
    # Проверен пустой блок заданий
    create_course_page.check_visible_exercises_empty_view()
    # Загружено изображение
    create_course_page.upload_preview_image("C:/Users/rain1/PycharmProjects/autotests-ui/testdata/files/image.jpg")
    # Проверен блок загрузки в состоянии после успешной загрузки
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    # Форма заполнена значениями
    create_course_page.fill_create_course_form(title="Playwright", description="Playwright", estimated_time="2 weeks", max_score="100", min_score="10")
    # Нажата кнопка создания курса
    create_course_page.click_create_course_button()

    # Проверен заголовок "Courses"
    courses_list_page.check_visible_courses_title()
    # Проверена кнопка создания курса
    courses_list_page.check_visible_create_course_button()
    # Проверена карточка созданного курса
    courses_list_page.check_visible_course_card(index=0, title="Playwright", estimated_time="2 weeks", max_score="100", min_score="10")
