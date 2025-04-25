import pytest
import json
import pytest
from ..data_faker import get_data
import yaml

from ..pages.register_page import RegisterPage
"""file_name = "/Users/snehas/PycharmProjects/PythonProject/Day15_MiniTestProjects/ShopSwift_DemoWebShop/testdata/data.json"

with open(file_name, 'r') as f:
     data = json.load(f)"""

"""file_name = "/Users/snehas/PycharmProjects/PythonProject/Day15_MiniTestProjects/ShopSwift_DemoWebShop/testdata/data.yaml"
with open(file_name, 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)"""

class TestRegister:
     def test_register(self, driver, get_data):
         rg = RegisterPage(driver)
         rg.navigate_url("https://demowebshop.tricentis.com/register")
         firstname, lastname, email, password = get_data  # clean unpacking
         """rg.register(data["firstname"], data["lastname"], data["email"], data["password"])"""
         rg.register(firstname, lastname, email, password)
         rg.expected_msg()
         rg.close_browser()


