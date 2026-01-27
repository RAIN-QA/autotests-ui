import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.sidebar.click_courses()
    courses_list_page.sidebar.check_visible()
    courses_list_page.navbar.check_visible("username")

    # Проверен заголовок "Courses" и кнопки создания курса
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    # Проверен заголовок "Create course"
    create_course_page.create_course_toolbar_view.check_visible()
    # Проверен блок загрузки изображения в состоянии без выбранной картинки
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    # Проверена форма со значениями по умолчанию
    create_course_page.create_course_form.check_visible(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0"
    )
    # Проверен заголовок "Exercises" и кнопка создания задания
    create_course_page.create_course_exercise_toolbar_view.check_visible()
    # Проверен пустой блок заданий
    create_course_page.check_visible_exercises_empty_view()
    # Загружено изображение
    create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.jpg")
    # Проверен блок загрузки в состоянии после успешной загрузки
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    # Форма заполнена значениями
    create_course_page.create_course_form.fill(
        title="Playwright",
        description="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )

    # Нажата кнопка создания курса
    create_course_page.create_course_toolbar_view.create_course_button.click()

    # Проверен заголовок "Courses" и кнопки создания курса
    courses_list_page.toolbar_view.check_visible()

    # Проверена карточка созданного курса
    courses_list_page.course_view.check_visible(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )