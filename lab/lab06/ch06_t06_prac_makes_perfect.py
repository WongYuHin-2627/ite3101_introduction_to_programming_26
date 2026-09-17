from typing import Any

def cube(number: int) -> int:
    return number*number*number


def by_three(n: int) -> any:
    if cube % 3 == 0:
        return cube(n)
    else:
        return False
