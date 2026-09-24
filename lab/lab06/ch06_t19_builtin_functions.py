def distance_from_zero(n: str):
    if type(n) is int or type(n) is float:
        return abs(n)
    else:
        return "Nope"
