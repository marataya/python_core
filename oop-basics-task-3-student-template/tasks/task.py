import math


class Counter:
    _count = 0
    _start = 0
    _stop = 0
    _max_reached = False

    def __init__(self, start = 0, stop = math.inf):
        self._count = self._start = start
        self._stop = stop

    def increment(self):
        self._max_reached = self._count >= self._stop
        self._count += 0 if self._max_reached else 1
        if self._max_reached:
            print("Maximal value is reached.")

    def get(self):
        return self._count

if __name__ == '__main__':
    c = Counter(start=42)
    c.increment()
    print(c.get())

    c = Counter()
    c.increment()
    print(c.get())
    # 1
    c.increment()
    print(c.get())
    # 2

    c = Counter(start=42, stop=43)
    c.increment()
    print(c.get())
    # 43

    c.increment()
    print(c.get())
    # Maximal value is reached.
    c.increment()
    print(c.get())
    # Maximal value is reached.
