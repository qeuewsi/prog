"""Простой консольный калькулятор."""

import math
import typing as tp

Number = tp.Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    >>> add(2, 3)
    5
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    >>> subtract(5, 3)
    2
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    >>> multiply(4, 2.5)
    10.0
    """
    return a * b


def divide(a: Number, b: Number) -> float:
    """
    >>> divide(10, 4)
    2.5
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b


def power(a: Number, b: Number) -> Number:
    """
    >>> power(2, 10)
    1024
    """
    return a**b


def square_root(a: Number) -> float:
    """
    >>> square_root(16)
    4.0
    """
    if a < 0:
        raise ValueError("Нельзя извлечь корень из отрицательного числа")
    return math.sqrt(a)


BINARY_OPERATIONS: tp.Dict[str, tp.Callable[[Number, Number], Number]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}

UNARY_OPERATIONS: tp.Dict[str, tp.Callable[[Number], Number]] = {
    "sqrt": square_root,
}


def calculate(operation: str, a: Number, b: tp.Optional[Number] = None) -> Number:
    """
    Выполняет операцию над числами.

    >>> calculate("+", 1, 2)
    3
    >>> calculate("sqrt", 9)
    3.0
    """
    if operation in BINARY_OPERATIONS:
        if b is None:
            raise ValueError(f"Для операции {operation} нужно два числа")
        return BINARY_OPERATIONS[operation](a, b)
    if operation in UNARY_OPERATIONS:
        return UNARY_OPERATIONS[operation](a)
    raise ValueError(f"Неизвестная операция: {operation}")


def parse_number(text: str) -> Number:
    """
    Превращает строку в число: целое, если возможно, иначе вещественное.

    >>> parse_number("42")
    42
    >>> parse_number("3,5")
    3.5
    """
    text = text.strip().replace(",", ".")
    try:
        return int(text)
    except ValueError:
        return float(text)


def main() -> None:
    """Цикл взаимодействия с пользователем."""
    operations = ", ".join(list(BINARY_OPERATIONS) + list(UNARY_OPERATIONS))
    print(f"Калькулятор. Доступные операции: {operations}. Для выхода введите q.")
    while True:
        operation = input("Операция: ").strip().lower()
        if operation in ("q", "quit", "exit"):
            break
        if operation not in BINARY_OPERATIONS and operation not in UNARY_OPERATIONS:
            print("Неизвестная операция, попробуйте ещё раз.")
            continue
        try:
            a = parse_number(input("Первое число: "))
            b = parse_number(input("Второе число: ")) if operation in BINARY_OPERATIONS else None
            print("Результат:", calculate(operation, a, b))
        except (ValueError, ZeroDivisionError) as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
