import allure
import pytest

from autotests.pages.data.main_data import roles
from autotests.pages.data.settings_data import settings_pages


@allure.feature('Login')
@allure.suite('Login page')
class TestLoginPage:
    @allure.story('Login page')
    @allure.title('Checking authorization via username and password [{role}]')
    @allure.label('layer', 'ui_tests')
    @pytest.mark.parametrize('role', [roles.admin])
    def test_login_page_login_via_username_and_password(self, role: str, login_page):
        """ Checking authorization via username and password - """
        login_page.login_by_password(role=role)

    @allure.story('Login page')
    @allure.title('Checking authorization via username and password [{case}][n]')
    @allure.label('layer', 'ui_tests')
    @pytest.mark.parametrize(
        'case, username, password',
        [
            ('empty_fields', '', ''),
            ('empty_username', '', 'test'),
            ('empty_password', 'test', ''),
            ('incorrect_password', 'parvin.ibrahimov', 'test'),
            ('script_username', '<script>alert(123)</script>', 'test'),
            ('html_tag_username', '<a>"Hello, World!"</a>', 'test'),
            ('symbols_username', '«♣☺♂»,«»‘~!@#$%^&*()?>,.<][/*<!—«»,«${code}»;—>', 'test'),
            ('spaces_username', '   ', 'test')
        ]
    )
    def test_login_page_negative_login_via_username_and_password(
            self, case: str, username: str, password: str, login_page):
        """ Checking authorization via username and password with incorrect data - """
        login_page.open_page(page='Password')
        login_page.fill_username(username=username)
        login_page.fill_password(password=password)
        login_page.click_btn_login()
        login_page.login_field_validation_check_negative(case=case)

    title = "Checking authorization via settings under user with role [{role}]"

    @allure.story('Login page')
    @allure.title('Checking authorization via settings under user with role [{role}]')
    @allure.label('layer', 'ui_tests')
    @pytest.mark.parametrize(
        'role', ['sales', 'negotiations', 'opener', 'accounting', 'enrollments', 'customer_service']
    )
    def test_login_page_login_as_user(self, role: str, login_page, settings_users_page):
        """ Checking authorization via settings under users with different roles - """
        login_page.login_by_password(role='admin', main_tab=None)
        login_page.click_dl_avatar()
        login_page.click_btn_settings()
        settings_users_page.change_settings_page(page=settings_pages.users, internal_title=True)
        settings_users_page.login_as_user(role=role)
