from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
import allure

class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page,'course-view-menu-button', "Menu")
        self.edit_menu_button = Button(page,'course-view-edit-menu-item', "Edit")
        self.delete_menu_button = Button(page,'course-view-delete-menu-item', "Delete")

    @allure.step('Click course menu at index "{index}" and click "Edit"')
    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_button.check_visible(nth=index)
        self.edit_menu_button.click(nth=index)

    @allure.step('Click course menu at index "{index}" and click "Delete"')
    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_button.check_visible(nth=index)
        self.delete_menu_button.click(nth=index)