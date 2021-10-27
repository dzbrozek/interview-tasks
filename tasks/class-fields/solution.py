class Test:
    x = 10


if __name__ == '__main__':
    a = Test()
    a.x = 1

    b = Test()

    assert a.x == 1
    assert b.x == 10

    Test.x = 5

    c = Test()

    assert a.x == 1
    assert b.x == 5
    assert c.x == 5
