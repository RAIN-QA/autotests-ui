import pytest
import allure

from allure_commons.types import Severity
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpics
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeatures
from pages.dashboard.dashboard_page import DashboardPage

@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTags.REGRESSION, AllureTags.DASHBOARD)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.DASHBOARD)
@allure.story(AllureStories.DASHBOARD)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeatures.DASHBOARD)
@allure.sub_suite(AllureStories.DASHBOARD)
class TestDashboard:
    @allure.title("Проверка отображения страницы Dashboard")
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

        dashboard_page_with_state.sidebar.click_dashboard()
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible("username")

        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_activities_chart()