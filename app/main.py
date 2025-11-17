from typing import Any


class Dictionary:

    def __init__(self, initial_size: int = 8) -> None:
        self.size = initial_size
        self.count = 0
        self.table = [None] * initial_size

    def __len__(self) -> int:
        return self.count

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % self.size

        while True:
            element = self.table[index]
            if element is None:
                raise KeyError(key)
            k, v = element
            if k == key:
                return v

            index = (index + 1) % self.size

    def __setitem__(self, key: Any, value: Any) -> None:
        if (self.count + 1) > self.size * (2 / 3):
            self._resize()

        index = hash(key) % self.size

        while True:
            element = self.table[index]

            if element is None:
                self.table[index] = (key, value)
                self.count += 1
                return
            k, v = element
            if k == key:
                self.table[index] = (key, value)
                return

            index = (index + 1) % self.size

    def _resize(self) -> None:
        old_table = self.table

        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for element in old_table:
            if element is not None:
                key, value = element
                self[key] = value
