"""
Pages package for Page Object Model classes.
Contains all page objects for the Sauce Demo application.
"""

from .base_page import BasePage
from .login_page import LoginPage
from .products_page import ProductsPage
from .cart_page import CartPage

__all__ = [
    'BasePage',
    'LoginPage', 
    'ProductsPage',
    'CartPage'
]
