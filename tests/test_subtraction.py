from src.calculator import subtract
import pytest
import allure

@allure.description("Testcase to substract positive")
def test_subtract_positive():
    result = subtract(4, 3)
    assert result == 1

