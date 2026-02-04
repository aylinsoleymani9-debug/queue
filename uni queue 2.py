class CQueue:
    def __init__(self, max):
        self.max = max
        self.list = [None] * max
        self.front = -1
        self.rear = -1

    def insert(self, x):
        if (self.rear + 1) % self.max == self.front:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[self.rear] = x
            print(f"Inserted {x}")
            return
        self.rear = (self.rear + 1) % self.max
        self.list[self.rear] = x
        print(f"Inserted {x}")

    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return
        k = self.list[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max
        print(f"Deleted {k}")
        return k

    def show_valid(self):
        if self.front == -1:
            print("Queue is empty")
            return
        print("Queue contents:", end=" ")
        if self.front <= self.rear:
            for i in range(self.front, self.rear + 1):
                print(self.list[i], end=" ")
        else:
            for i in range(self.front, self.max):
                print(self.list[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.list[i], end=" ")
        print()

    def show_invalid(self):
        if self.front == -1:
            for i in range(len(self.list)):
                print(self.list[i])
            return
        i = (self.rear + 1) % len(self.list)
        while i != self.front:
            print(self.list[i])
            i = (i + 1) % len(self.list)

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % len(self.list) == self.front

    def find(self, x):
        k = []
        if self.is_empty():
            return
        i = self.front
        if self.list[i] == x:
            k.append(i)
        while i != self.rear:
            i = (i + 1) % len(self.list)
            if self.list[i] == x:
                k.append(i)
        return k

    def replace(self, x, y):
        if self.is_empty():
            return
        i = self.front
        if self.list[i] == x:
            self.list[i] = y
        while i != self.rear:
            i = (i + 1) % len(self.list)
            if self.list[i] == x:
                self.list[i] = y
