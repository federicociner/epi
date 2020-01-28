import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple("Rect", ("x", "y", "width", "height"))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    def is_intersect(r1: Rect, r2: Rect):
        is_r1_less_width = r1.x <= r2.x + r2.width
        is_r1_greater_width = r1.x + r1.width >= r2.x
        is_r1_less_height = r1.y <= r2.y + r2.height
        is_r1_greater_height = r1.y + r1.height >= r2.y

        return (
            is_r1_less_height
            and is_r1_greater_height
            and is_r1_less_width
            and is_r1_greater_width
        )

    if not is_intersect(r1, r2):
        return Rect(0, 0, -1, -1)

    x = max(r1.x, r2.x)
    y = max(r1.y, r2.y)
    width = min(r1.x + r1.width, r2.x + r2.width) - x
    height = min(r1.y + r1.height, r2.y + r2.height) - y

    return Rect(x, y, width, height)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            "rectangle_intersection.tsv",
            intersect_rectangle_wrapper,
            res_printer=res_printer,
        )
    )
