from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
driver.find_element(By.NAME, "Gender").click()
driver.find_element(By.NAME, "FirstName").send_keys("sn")
driver.find_element(By.NAME, "LastName").send_keys("s")
driver.find_element(By.NAME, "Email").send_keys("sneha1@example.com")
driver.find_element(By.NAME, "Password").send_keys("sneha123")
driver.find_element(By.NAME, "ConfirmPassword").send_keys("sneha123")
driver.find_element(By.ID, "register-button").click()
expected_success_msg = driver.find_element(By.XPATH, "//div[@class='result']").text
assert "Your registration completed".strip() in expected_success_msg.strip()