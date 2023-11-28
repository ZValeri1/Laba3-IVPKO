import fromlaba2Library
import pytest

# Тесты для функции определения n чисел Фибоначчи
def test_fibonacci_numbers():
    assert fromlaba2Library.fibonacci_numbers(5) == [0, 1, 1, 2, 3]
    assert fromlaba2Library.fibonacci_numbers(8) == [0, 1, 1, 2, 3, 5, 8, 13]

# Тесты для функции сортировки пузырьком
def test_bubble_sort():
    assert fromlaba2Library.bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert fromlaba2Library.bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Тесты для функции калькулятора
def test_calculator():
    # Корректные входные данные
    assert fromlaba2Library.calculator(5, 3, '+') == 8
    assert fromlaba2Library.calculator(5, 3, '-') == 2
    assert fromlaba2Library.calculator(5, 3, '*') == 15
    assert fromlaba2Library.calculator(6, 2, '/') == 3.0
    assert fromlaba2Library.calculator(6, 0, '/') == "Error: Division by zero"
    assert fromlaba2Library.calculator(6, 2, '@') == "Error: Invalid operation"

    # Граничные значения
    assert fromlaba2Library.calculator(0, 0, '+') == 0
    assert fromlaba2Library.calculator(-1, 1, '-') == -2
    assert fromlaba2Library.calculator(10, 0, '*') == 0
    assert fromlaba2Library.calculator(10, 0, '/') == "Error: Division by zero"

pytest.main()