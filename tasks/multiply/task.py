def multiply_by_2():
    pass


@multiply_by_2
def calculate1(n):
    return n + 1


def multiply_by_n():
    pass


@multiply_by_n(4)
def calculate2(n):
    return n + 1


if __name__ == "__main__":
    assert calculate1(3) == 8
    assert calculate2(3) == 16

