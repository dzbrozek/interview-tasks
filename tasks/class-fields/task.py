class Test:
    x = 10


if __name__ == '__main__':
    a = Test()
    a.x = 1

    b = Test()

    assert a.x == 'update value'
    assert b.x == 'update value'

    Test.x = 5

    c = Test()

    assert a.x == 'update value'
    assert b.x == 'update value'
    assert c.x == 'update value'
