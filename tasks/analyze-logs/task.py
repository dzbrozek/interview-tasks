from typing import List, Tuple

logs = [
    ('192.0.0.1', '/api/test/', 100),
    ('192.0.0.3', '/api/test2/', 200),
    ('192.0.0.2', '/api/test/', 300),
    ('192.0.0.2', '/api/test2/', 50),
    ('192.0.0.3', '/api/test/', 100),
    ('192.0.0.2', '/api/test3/', 500)
]


def analyze_logs(logs: List[Tuple[str, str, int]]) -> str:
    """find the slowest endpoint"""
    pass


if __name__ == '__main__':
    assert analyze_logs(logs) == '/api/test3/'
