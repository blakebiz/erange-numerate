class erange:
    def __init__(self, *args):
        if any([arg for arg in args if not isinstance(arg, int)]): raise TypeError("Input must be int")
        if len(args) == 0:
            raise Exception("you gave no arguments")
        elif len(args) == 1:
            self.start, self.stop, self.step = 0, args[0], 1
        elif len(args) == 2:
            self.start, self.stop, self.step = args[0], args[1], 1
        elif len(args) == 3:
            self.start, self.stop, self.step = args[0], args[1], args[2]
        else:
            raise Exception("Too many arguments given")
        self._start = self.start
        if self.step == 0: raise ValueError("step of 0 given")
    def __iter__(self):
        return self
    def __next__(self):
        if self.step > 0:
            condition = self.start < self.stop
        else:
            condition = self.start > self.stop
        if not condition:
            self.start = self._start
            raise StopIteration
        self.start += self.step
        return self.start - self.step
    def __str__(self):
        return f'range({self.start}, {self.stop})'
    def __getitem__(self, item):
        result = (item * self.step) + self.start
        if self.step > 0:
            condition = result < self.stop
        else:
            condition = result > self.stop
        if condition:
            return result
        else:
            raise IndexError("Invalid index given")
    def __len__(self):
        # if it is evenly divisible, return value, else return value + 1
        if ((self.stop - self.start) // self.step) == ((self.stop - self.start) / self.step):
            return (self.stop - self.start) // self.step
        else:
            return ((self.stop - self.start) // self.step) + 1
    def __eq__(self, other):
        return self.start == other.start and self.stop == other.stop and self.step == other.step if isinstance(other, erange) else False
    __repr__ = __str__



def numerate(iterable, start=0):
    for item in iterable: yield start, item; start += 1

# Can even be indexed like range
print(erange(1, 10)[3])
print(range(1, 10)[3])
# Even shows equality
print(erange(1, 10) == erange(1, 9))
print(range(1, 10) == range(1, 9))
print(erange(1, 10) == erange(1, 10))
print(range(1, 10) == range(1, 10))
# Has length too
print(len(erange(10)))
print(len(range(10)))
# Even prints the same
print(erange(1, 10))
print(range(1, 10))
# Passes all normal tests too
print('erange')
for i in erange(3):
    print(i)
print('range')
for i in range(3):
    print(i)
print('\nerange')
for i in erange(1, 4):
    print(i)
print('range')
for i in range(1, 4):
    print(i)
print('\nerange')
for i in erange(1, 6, 2):
    print(i)
print('range')
for i in range(1, 6, 2):
    print(i)
print('erange')
for i in erange(6, 1, -2):
    print(i)
print('range')
for i in range(6, 1, -2):
    print(i)
