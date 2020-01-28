from test_framework import generic_test


def power(x: float, y: int) -> float:
    res = 1.0
    power = y

    if y < 0:
        power = -power
        x = 1.0 / x

    while power:
        if power & 1:
            res *= x
        x *= x
        power >>= 1

    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main("power_x_y.py", "power_x_y.tsv", power)
    )
