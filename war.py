from typing import List, Optional
from functools import total_ordering, reduce
import csv
import random


class Player:
    name: str

    def __init__(self, name: str):
        self.name = name


@total_ordering
class Chemical:
    """A chemical composed of multiple elements."""

    _contents: List[Element]

    def __init__(self) -> None:
        self._contents = []

    def mass(self) -> float:
        return reduce(lambda c, n: c + n.mass(), self._contents, 0)

    def __add__(self, other: Element) -> "Chemical":
        a = Chemical()
        a._contents = self._contents.copy()
        a._contents.append(other)
        return a

    def __repr__(self) -> str:
        return f"Chemical is composed of " + ", ".join(
            map(lambda c: repr(c), self._contents)
        )

    def __lt__(self, other: "Chemical") -> bool:
        return self.mass() < other.mass()


class Element:
    """A chemical element."""

    _name: str
    _mass: float

    def __init__(self, name: str, atomic_mass: float) -> None:
        self._name = name
        self._mass = atomic_mass

    def name(self) -> str:
        return self._name

    def mass(self) -> float:
        return self._mass

    def __repr__(self) -> str:
        return f"{self.name()} (mass: {self.mass()})"

    def __add__(self, other: "Element") -> Chemical:
        c = Chemical()
        c._contents = [self, other]
        return c


class PeriodicTable:
    """The Periodic Table of elements."""

    _table: List[Element]

    def __init__(self, filename: str):
        self._table = []
        with open(filename, mode="r") as f:
            for l in csv.reader(f):
                element = Element(l[2], float(l[3]))
                self._table.append(element)

    def random(self) -> Optional[Element]:
        if len(self._table) == 0:
            return None
        r = random.randint(0, len(self._table) - 1)
        self._table[-1], self._table[r] = self._table[r], self._table[-1]
        try:
            return self._table.pop()
        except IndexError as e:
            return None


class Game:
    """A game of War!"""

    _players: List[Player]

    def __init__(self, p1: Player, p2: Player):
        pass


if __name__ == "__main__":
    # This is where we write code that
    # executes when the program starts.
    pass