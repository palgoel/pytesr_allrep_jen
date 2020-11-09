from src.calculator import subtract
import pytest
import allure

@allure.description("Testcase to substract positive")
def test_subtract_positive():
    result = subtract(4, 3)
    assert result == 1

@allure.description("Testcase to substract nagative")
def test_subtract_negative():
    result = subtract(3, 4)
    assert result == -1

@allure.description("Testcase to substract String")
def test_subtract_string():
    with pytest.raises(TypeError):
        subtract("string", 4)
