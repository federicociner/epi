import string
from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    is_negative = False

    if x < 0:
        x = -x
        is_negative = True

    s = []

    while True:
        s.append(chr(ord("0") + x % 10))
        x //= 10
        if x == 0:
            break

    return f"{('-' if is_negative else '')}{''.join(reversed(s))}"


def string_to_int(s: str) -> int:
    res = 0

    for digit in s:
        if digit not in list(string.digits):
            continue

        res = (res * 10) + string.digits.index(digit)

    return res * -1 if s[0] == "-" else res


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )
