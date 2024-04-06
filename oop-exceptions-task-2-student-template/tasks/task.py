from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    try:
        a, b = map(int, str_with_ints.split())
        return a / b
    except ZeroDivisionError:
        return "Error code: division by zero"
    except ValueError as e:
        return f"Error code: {e}"

if __name__ == '__main__':
    print(divide("4 2"))
    # 2.0

    print(divide("4 0"))
    # "Error code: division by zero"

    print(divide("* 1"))
    # "Error code: invalid literal for int() with base 10: '*'"
