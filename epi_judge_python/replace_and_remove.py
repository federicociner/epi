import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    a_count = 0
    write_idx = 0

    # Remove "b"s and count "a"s
    for i in range(size):
        if s[i] != "b":
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == "a":
            a_count += 1

    # Replace "a"s with "dd"s
    curr_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1

    while curr_idx >= 0:
        if s[curr_idx] == "a":
            s[write_idx - 1 : write_idx + 1] = "dd"
            write_idx -= 2
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1
        curr_idx -= 1

    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "replace_and_remove.py",
            "replace_and_remove.tsv",
            replace_and_remove_wrapper,
        )
    )
