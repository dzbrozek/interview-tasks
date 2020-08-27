from functools import wraps


def html_tag(tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'

        return wrapper
    return decorator


@html_tag('p')
def foobar():
    return 'foobar'


if __name__ == "__main__":
    assert foobar() == '<p>foobar</p>'
    assert foobar.__name__ == 'foobar'

