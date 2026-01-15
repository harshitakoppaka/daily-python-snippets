"""
Day 03 - Dictionary Utilities
"""

def invert_dict(d: dict) -> dict:
    """Invert keys and values of a dictionary."""
    return {value: key for key, value in d.items()}


def merge_dicts(a: dict, b: dict) -> dict:
    """Merge two dictionaries (b overrides a)."""
    merged = a.copy()
    merged.update(b)
    return merged


if __name__ == "__main__":
    print(invert_dict({"a": 1, "b": 2}))
    print(merge_dicts({"x": 1, "y": 2}, {"y": 3, "z": 4}))
