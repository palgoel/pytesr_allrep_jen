from src.calculator import add
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure

global driver

@allure.description("Testcase to add num")
@allure.severity(severity_level="CRITICAL")
def test_add():

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://www.google.com")
        handle = driver.current_window_handle
#         try:
#             assert "1" in handle
#         finally:
#           if(AssertionError):
#             allure.attach(driver.get_screenshot_as_png(),name="Handle is wrong", attachment_type=allure.attachment_type.PNG)
#         driver.quit()
@allure.description("Testcase to add String")
@allure.severity(severity_level="NORMAL")
def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)
