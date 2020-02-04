from typing import List

from test_framework import generic_test, test_utils


digit_map = {
    "0": "0",
    "1": "1",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
}


def phone_mnemonic(phone_number: str) -> List[str]:
    if not phone_number:
        return []

    prev = list(digit_map[phone_number[0]])

    for i in range(1, len(phone_number)):
        curr = []

        for c in digit_map[phone_number[i]]:
            curr += [cc + c for cc in prev]

        prev = curr

    return prev


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            "phone_number_mnemonic.tsv",
            phone_mnemonic,
            comparator=test_utils.unordered_compare,
        )
    )
