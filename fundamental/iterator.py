class Counter(object):
    def __init__(self, start, end):
        self._current = start
        self._end = end

    def __iter__(self):
        while self._current < self._end:
            yield self._current
            self._current += 1


count = Counter(10, 50)
for i in count:
    print(i)
