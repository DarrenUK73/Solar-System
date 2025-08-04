class Multipler:
    def __init__(self, v1, v2):
        self._first = v1
        self._second = v2

    def square(self, p):
        print(f"1. in square. The value of p is {p}")
        if p == 0:
            print(f"2. p is zero")
            return self._first * self._first
        else:
            print(f"3. p is NOT zero")
            return self._first * self._first

multy = Multipler(3, 4)
x = multy.square(1) 
assert x == 16 
