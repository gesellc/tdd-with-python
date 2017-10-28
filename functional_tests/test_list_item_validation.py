from unittest import skip
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import unittest
import time

class ItemValidationTest(FunctionalTest):

    def _get_error_element(self):
        time.sleep(1)
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error = self._get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys('')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        self.wait_for_row_in_list_table('1: Buy milk')
        error = self._get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy wellies')

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # She sees a helpful error message
        self.wait_for_row_in_list_table('1: Buy wellies')
        error = self._get_error_element()
        self.assertEqual(error.text, "You've already got this on your list")

    def test_error_messages_are_cleared_on_input(self):
        # Edith starts a new list in a way that causes a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('')
        self.get_item_input_box().send_keys(Keys.ENTER)
        error = self._get_error_element()
        self.assertTrue(error.is_displayed())

        # She starts typeing in the input box to clear the error
        self.get_item_input_box().send_keys('a')

        # She is pleased to see that the error message dissappears
        error = self._get_error_element()
        self.assertFalse(error.is_displayed())
