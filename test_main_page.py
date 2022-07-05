from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

main_page_link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, main_page_link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_and_register_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_not_be_full()
    basket_page.should_be_empty()

