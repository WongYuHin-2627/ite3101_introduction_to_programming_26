def cube(n: int):
    return n*n*n


def by_three():
    if cube % 3 == 0:
        return "cube%3"
    else:
        return False
