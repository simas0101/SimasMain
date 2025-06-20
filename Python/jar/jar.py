class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies")
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity is less than 1")
        self._capacity = capacity
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size is greater than capacity")
        self._size = size

def main():
        jar = Jar()
        print(jar)
        jar.deposit(3)
        print(jar)
        jar.withdraw(2)
        print(jar)


if __name__ == "__main__":
    main()
