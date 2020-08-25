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
    if not logs:
        return ''

    stats = {}
    for _, endpoint, time in logs:
        if endpoint not in stats:
            stats[endpoint] = []

        stats[endpoint].append(time)

    return sorted(stats.items(), key=lambda item: sum(item[1]) / len(item[1]), reverse=True)[0][0]


if __name__ == '__main__':
    print('The slowest endpoint is:', analyze_logs(logs))
    assert analyze_logs(logs) == '/api/test3/'
