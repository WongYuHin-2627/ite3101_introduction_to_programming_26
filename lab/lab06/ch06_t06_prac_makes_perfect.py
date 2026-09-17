def cube(n: int) -> int:
    return n*n*n


def by_three(n: int) -> any:
    if cube % 3 == 0:
        return cube(n)
    else:
        return False
