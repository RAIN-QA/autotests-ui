from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page,'create-course-toolbar-title-text', "Title")
        self.create_course_button = Button(page,'create-course-toolbar-create-course-button', "Create course")

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Create course')

        self.create_course_button.check_visible()


    # def check_visible(self, is_edit_mode: bool = False):
    #     self.title.check_visible()
    #     if is_edit_mode:
    #         self.title.check_have_text('Update course')
    #         self.create_course_button.check_have_text('Update course')
    #     else:
    #         self.title.check_have_text('Create course')
    #         self.create_course_button.check_have_text('Create course')
    #
    #     self.create_course_button.check_visible()

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_disabled_create_course_button(self):
        self.create_course_button.check_disabled()