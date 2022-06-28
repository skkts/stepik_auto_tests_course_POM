import time
import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
urls = [f"{base_link}?promo=offer{n}" if n != 7
        else pytest.param("bugged_link", marks=pytest.mark.xfail) for n in range(10)]

@pytest.mark.parametrize("link", urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_matches_book_names()
    page.should_matches_book_prices()

