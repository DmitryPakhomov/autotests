import os
import random
import sys
import time
import random
import allure
from allure_commons.types import AttachmentType
from typing import Union, NoReturn, Any


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from autotests.pages.base import WebPage
from autotests.pages.settings import Settings
from autotests.pages.utils import compress_image


class Element(WebPage):
    """
    Class for performing actions with page elements.
    """

    def find_element(
            self,
            locator: tuple[str, str],
            t: Union[int, float] = 10,
            many: bool = False
    ) -> Union[WebElement, list[WebElement]]:
        """
        A method to search for and retrieve a web element or a list of web elements.

        :param locator: Locator, to search for a web element.
        :param t: Time, for retrieving a web element.
        :param many: To retrieve a single web element or a list of web elements.
        :return: A web element or a list of web elements.
        """
        if many:
            return WebDriverWait(self.driver, t).until(
                ec.presence_of_all_elements_located(locator),
                message=f"On the page {self.get_current_page_url()}, "
                        f"no elements found with locator {locator}"
            )
        return WebDriverWait(self.driver, t).until(
            ec.presence_of_element_located(locator),
            message=f"On the page {self.get_current_page_url()}, "
                    f"no element found with locator {locator}"
        )

    def click_element(self, locator: tuple[str, str], t: Union[int, float] = 10) -> NoReturn:
        """
        A method to search for and click a web element or a list of web elements.

        :param locator: Locator, to search for a web element.
        :param t: Time, for retrieving a web element.
        """
        self.find_element(locator=locator, t=t).click()

    def select_element(
            self,
            locator: tuple[str, str],
            text: str = '',
            index: int = '',
            value: str = ''
    ) -> NoReturn:
        """
        Method to select an element from a drop-down list.

        :param locator: Locator, to find the web element.
        :param text: The text of the element from the list.
        :param index: Index of the element from the list.
        :param value: The value of the item in the list.
        """
        select = Select(self.find_element(locator))
        if text:
            select.select_by_visible_text(text)
        if index:
            select.select_by_index(index)
        if value:
            select.select_by_value(value)

    def get_selected_value(self, locator: tuple[str, str]) -> str:
        """
        Method to get the value of the selected element from the list.

        :param locator: Locator to find the web element.
        :return: Value of the selected element
        """
        select = Select(self.find_element(locator))
        selected_option = select.first_selected_option.text
        return selected_option

    def click_via_js(self, elem: WebElement) -> None:
        """
        Method for clicking on an element via JavaScript code execution.

        :param elem: The web element to be clicked.
        """
        self.driver.execute_script("arguments[0].click();", elem)

    def click_via_js_new(self, elem: WebElement) -> None:
        """
        Method for clicking on an element via JavaScript code execution new version.

        :param elem: The web element to be clicked.
        """
        self.driver.execute_script("arguments[0].setAttribute('data-clicked', 'true'); arguments[0].click();", elem)

    def element_is_present(self, locator: tuple[str, str], t: Union[int, float] = 1) -> bool:
        """
        A method to check if a web element is present in the DOM.

        :param locator: Locator, to find the web element.
        :param t: Time to check.
        :return: True or False.
        """
        # noinspection PyBroadException
        try:
            self.find_element(locator, t)
        except Exception:
            return False
        return True

    def element_is_displayed(self, locator: tuple[str, str], t: Union[int, float] = 1) -> bool:
        """
        Method to check the visibility of the web element.

        :param locator: Locator, to find the web element.
        :param t: Time to check.
        :return: True or False.
        """
        elem = self.find_element(locator, t)
        if elem:
            return elem.is_displayed()
        return False

    def element_is_clickable(
            self, locator: tuple[str, str], t: Union[int, float] = 1
    ) -> bool:
        """
        Method to check the clickability of a web element.

        :param locator: Locator, to find the web element.
        :param t: Time to check.
        :return: True or False.
        """
        # noinspection PyBroadException
        try:
            self.wait_until_element_to_be_clickable(locator, t)
        except Exception:
            return False
        return True

    def wait_until_element_not_visible(
            self,
            locator: tuple[str, str],
            t: Union[int, float] = 10
    ) -> WebElement:
        """
        Method to wait for the visibility of the web element.

        :param locator: Locator, to find the web element.
        :param t: Time to check.
        :return: web element.
        """
        elem = self.find_element(locator, t)
        if elem:
            js = (
                'return (!(arguments[0].offsetParent === null) && '
                '!(window.getComputedStyle(arguments[0]) === "none") &&'
                'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0);'
            )
            visibility = self.driver.execute_script(js, elem)
            iteration = 0

            while not visibility and iteration < 10:
                time.sleep(0.5)
                iteration += 1
                visibility = self.driver.execute_script(js, elem)

        return elem

    def wait_until_element_to_be_clickable(
            self,
            locator: tuple[str, str],
            t: Union[int, float] = 10
    ) -> WebElement:
        """
        Method to expect the clickability of a web element.

        :param locator: Locator, to find the web element.
        :param t: Time to check.
        :return: web element.
        """
        return WebDriverWait(self.driver, t).until(
            ec.element_to_be_clickable(locator),
            message=f"Element is not clickable: {locator}"
        )

    def wait_until_element_visible(
            self,
            locator: tuple[str, str],
            t: Union[int, float] = 10
    ) -> WebElement:
        """
        Method to expect the clickability of a web element.

        :param locator: Locator, to find the web element.
        :param t: Time to check.
        :return: web element.
        """
        return WebDriverWait(self.driver, t).until(
            ec.visibility_of_element_located(locator),
            message=f"Element is not visible: {locator}"
        )

    def send_keys(
            self,
            locator: tuple[str, str],
            keys: list[Any],
            clear: bool = True,
            javascript: bool = False,
            t: Union[int, float] = 0.1
    ) -> NoReturn:
        """
        A method to pass keys or a value to a web element.

        :param locator: Locator, to find the web element.
        :param keys: list of actions(keys(Keys.CTRL + 'v') or value('test')).
        :param clear: clearing text in a field.
        :param javascript: type value using javascript.
        :param t: Wait time after input.
        """
        elem = self.find_element(locator)
        elem.click()
        if clear:
            elem.clear()
        for key in keys:
            elem.send_keys(key)
        if javascript:
            value = ''.join(map(str, keys))
            self.driver.execute_script("arguments[0].value = arguments[1];", elem, value)
        time.sleep(t)

    def get_text(
            self, locator: tuple[str, str], many: bool = False, lower: bool = False
    ) -> str | list[str]:
        """
        Method to retrieve the text.

        :param lower:
        :param locator: Locator, to find a web element.
        :param many: To retrieve the text of a single web element or a list of web elements.
        :return: text.
        """
        texts = []
        elem = self.find_element(locator=locator, many=many)

        if many:
            for i in elem:
                if str(i.text):
                    texts.append(i.text.strip().lower() if lower else i.text.strip())
            return texts
        return elem.text.strip().lower() if lower else elem.text.strip()

    def get_attribute(
            self,
            locator: tuple[str, str],
            attr_name: str,
            many: bool = False
    ) -> Any:
        """
        Method to get the value of a web element attribute.

        :param locator: Locator, to find the web element.
        :param attr_name:
        :param many: To get the attribute value of a single
        of a single web element or a list of web elements.
        :return: The value of an attribute of a single web element or a list of web elements.
        """
        attr_values = []
        elem = self.find_element(locator, many)
        if many:
            for i in elem:
                attr_values.append(i.get_attribute(attr_name))
            return attr_values
        return elem.get_attribute(attr_name)

    def get_property(
            self,
            locator: tuple[str, str],
            property_name: str,
            many: bool = False,
            lower: bool = False
    ) -> Any:
        """
        Method to get the value of the web element properties.

        :param lower:
        :param locator: Locator, to find the web element.
        :param property_name: Property name
        :param many: to get the property value of a single web element or a list of web elements.
        web element or a list of web elements.
        :return: The property value of a single web element or a list of web elements.
        """
        property_values = []
        elem = self.find_element(locator, many)

        if many:
            for i in elem:
                text = str(i.get_property(property_name))
                property_values.append(text.strip().lower() if lower else text.strip())
            return property_values
        return elem.get_property(property_name).strip().lower() if lower \
            else elem.get_property(property_name).strip()

    def scroll_to_elem(self, elem: WebElement) -> NoReturn:
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)

    def highlight_element(self, elem: WebElement, scroll: bool = False, error: bool = False) -> NoReturn:
        # Scrolls the page to a specified web element:
        if scroll:
            self.scroll_to_elem(elem=elem)
        # Highlights the specified web element, with a green or red frame:
        color = 'green'
        if error:
            color = 'red'
        self.driver.execute_script(f"arguments[0].style.border='2px solid {color}'", elem)

    def highlight_and_make_screenshot(
            self,
            locators: list[tuple[str, str]] = None,
            elem: WebElement = None,
            file_name: str = 'screen',
            scroll: bool = False,
            error: bool = False,
            remove_screen: bool = True,
            step_title: str = 'Make screenshot.'
    ) -> NoReturn:
        """
        Method for screenshots.

        :param step_title:
        :param scroll:
        :param locators: Locator, for finding a web element.
        :param elem: Web element
        :param file_name: The name for the screen, by default screen.png.
        :param error: For error screen.
        :param remove_screen: Remove screenshot.
        """
        if locators:
            for locator in locators:
                elem = self.find_element(locator)
                self.highlight_element(elem, scroll=scroll, error=error)
        if elem:
            self.highlight_element(elem, scroll=scroll, error=error)

        screenshot = self.driver.get_screenshot_as_png()
        with allure.step(step_title):
            allure.attach(compress_image(screenshot), name=file_name, attachment_type=AttachmentType.JPG)

    def click_elem_by_text(self, tag: str, text: str, t: int = 10) -> NoReturn:
        """
        Method of clicking on an element by element tag and text.

        Example:
        element: <div class="rac-button__content">All</div>
        method call: self.click_elem_by_text(tag='div', text='All')

        :param t:
        :param tag: element tag.
        :param text: element text.
        """
        self.find_element((By.XPATH, f"//{tag}[contains(text(), '{text}')]"), t).click()

    def double_click_elem_by_text(self, tag: str, text: str, t: int = 1) -> NoReturn:
        """
        Method of clicking on an element by element tag and text.

        Example:
        element: <div class="rac-button__content">All</div>
        method call: self.click_elem_by_text(tag='div', text='All')

        :param t:
        :param tag: element tag.
        :param text: element text.
        """
        elem = self.find_element((By.XPATH, f"//{tag}[contains(text(), '{text}')]"), t)
        action = ActionChains(self.driver)
        action.double_click(elem).perform()

    def click_elem_by_link_text(self, text: str) -> NoReturn:
        """
        Method of clicking on a link by part of the link text

        Example:
        element: <div class="rac-button__content">All</div>
        method call: self.click_elem_by_link_text(text='All')

        :param text: link text.
        """
        self.find_element((By.PARTIAL_LINK_TEXT, text)).click()

    def get_elem_by_text(self, tag: str, text: str) -> WebElement:
        """
        A method for retrieving an element by element tag and text.

        Example:
        Element: <div class="rac-button__content">All</div>
        method call: self.click_elem_by_text(tag='div', text='All')

        :param tag: element tag.
        :param text: element text.
        :return: web element.
        """
        return self.find_element((By.XPATH, f"//{tag}[contains(text(), '{text}')]"))

    @staticmethod
    def get_locator_by_text(tag: str, text: str) -> tuple[str, str]:
        """
        Method of getting element locator by element tag and text.

        Example:
        Element: <div class="rac-button__content">All</div>
        method call: self.click_elem_by_text(tag='div', text='All')

        :param tag: element tag.
        :param text: element text.
        :return: web element locator.
        """
        return By.XPATH, f"//{tag}[contains(text(), '{text}')]"
