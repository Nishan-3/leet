from bisect import bisect_right, insort
from typing import Dict, List, Tuple

class TimeMap:
    """
    Time-based key-value store.

    - set(key, value, timestamp): store value for key at timestamp.
    - get(key, timestamp): return value associated with the largest timestamp <= given timestamp,
                           or "" if none exists.

    By default this class assumes timestamps for each key are provided in non-decreasing order
    (common in many problem statements). If you cannot guarantee that, pass
    assume_sorted_timestamps=False when constructing the object and the code will insert
    out-of-order timestamps correctly (costlier: O(n) insertion).
    """

    def __init__(self, assume_sorted_timestamps: bool = True):
        # store: key -> List[ (timestamp, value) ], sorted by timestamp
        self.store: Dict[str, List[Tuple[int, str]]] = {}
        self.assume_sorted = assume_sorted_timestamps

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        if self.assume_sorted:
            # append is O(1) when timestamps are non-decreasing
            self.store[key].append((timestamp, value))
        else:
            # Insert into the sorted list at correct position (O(n) insertion)
            insort(self.store[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Return the value with the largest timestamp <= given timestamp, or "" if none.
        Uses binary search (bisect_right) to find the insertion point.
        """
        values = self.store.get(key)
        if not values:
            return ""

        # values is a list of (timestamp, value). We want the rightmost item with ts <= timestamp.
        # bisect_right returns index where (timestamp, ...) would be inserted to keep order.
        idx = bisect_right(values, (timestamp, chr(255)))  # chr(255) ensures tie behavior
        if idx == 0:
            return ""         # all stored timestamps > requested timestamp
        return values[idx - 1][1]
