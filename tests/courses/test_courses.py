import pytest
import allure

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage

from allure_commons.types import Severity
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpics
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures
from tools.routes import AppRoute
from config import settings


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTags.REGRESSION, AllureTags.COURSES)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.COURSES)
@allure.story(AllureStories.COURSES)
@allure.severity(Severity.NORMAL)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeatures.COURSES)
@allure.sub_suite(AllureStories.COURSES)
class TestCourses:
    @allure.title("Проверка отображения пустого списка курсов")
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)

        courses_list_page.sidebar.click_courses()
        courses_list_page.sidebar.check_visible()
        courses_list_page.navbar.check_visible(settings.test_user.username)

        # Проверен заголовок "Courses" и кнопки создания курса
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()


    @allure.title("Проверка создания курса")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.COURSES_CREATE)
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
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
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
        create_course_page.create_course_toolbar_view.click_create_course_button()

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

    @allure.title("Проверка редактирования курса")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.COURSES_CREATE)
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            description="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

        # Нажатие на кнопку Edit через меню карточки курса
        courses_list_page.course_view.menu.click_edit(index=0)

        # Изменение полей курса
        create_course_page.create_course_form.fill(
            title="Playwright Updated",
            description="Updated Playwright course description",
            estimated_time="3 weeks",
            max_score="150",
            min_score="20"
        )

        # Нажатие на кнопку сохранения изменений
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # Проверка, что отображается карточка курса с обновленными данными
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright Updated",
            estimated_time="3 weeks",
            max_score="150",
            min_score="20"
        )

