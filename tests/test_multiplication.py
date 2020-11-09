from src.calculator import multiply
import pytest
import allure

@allure.description("Testcase to multiply")
def test_multiply():
    result = multiply(3, 4)
    assert result == 12

@allure.description("Testcase to multiply string")
def test_multiply_string():
    with pytest.raises(TypeError):
        multiply("string", 4)
