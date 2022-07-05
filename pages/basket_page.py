from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "'basket' is absent in the url"

    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING), "basket in not empty"

    def should_not_be_full(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM), "basket should be empty but it's not"