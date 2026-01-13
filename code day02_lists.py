"""
Day 02 - List Utilities
"""

def remove_duplicates(items: list) -> list:
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten_list(nested: list) -> list:
    """Flatten a list of lists."""
    return [item for sublist in nested for item in sublist]


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 1, 4]))
    print(flatten_list([[1, 2], [3, 4], [5]]))
