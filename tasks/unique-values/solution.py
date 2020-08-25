from collections import Counter

from typing import List, Any


def unique_values(elements: List[Any]):
    counter = Counter(elements)

    return [key for key, value in counter.items() if value == 1]


if __name__ == '__main__':
    assert unique_values([1, 2, 3, 2, 5, 1]) == [3, 5]
