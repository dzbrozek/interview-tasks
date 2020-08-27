def divisible(start, stop, by):
    while start <= stop:
        if start % by == 0:
            yield start
        start += 1


if __name__ == "__main__":
    assert list(divisible(0, 20, 7)) == [0, 7, 14]

    assert list(divisible(5, 10, 15)) == []
