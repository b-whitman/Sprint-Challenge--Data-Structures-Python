class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # Create a list to hold values
        self.buffer = [None for i in range(capacity)]
        # Create a cursor to track insert position
        self.cursor = 0

    def append(self, item):
        self.buffer[self.cursor] = item
        self.cursor += 1
        if self.cursor == self.capacity:
            self.cursor = 0

    def get(self):
        return [i for i in self.buffer if i!=None]
