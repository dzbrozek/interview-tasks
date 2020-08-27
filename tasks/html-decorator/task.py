def html_tag():
    # write body of decorator
    pass


@html_tag('p')
def foobar():
    return 'foobar'


if __name__ == "__main__":
    assert foobar() == '<p>foobar</p>'
