from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_matches_book_names(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_text = book_name.text
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET)
        book_name_in_basket_text = book_name_in_basket.text
        assert book_name_text == book_name_in_basket_text, "The names of book doesn't match"

    def should_matches_book_prices(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price_text = book_price.text
        book_price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET)
        book_price_in_basket_text = book_price_in_basket.text
        assert book_price_text == book_price_in_basket_text, "The cost of book doesn't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message doesn't disappear"
