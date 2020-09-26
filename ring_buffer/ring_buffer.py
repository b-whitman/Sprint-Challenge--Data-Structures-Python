class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # Create a list to hold values
        self.buffer = [None for i in range(capacity)]
        # Create a cursor to track insert position
        self.cursor = 0

    def append(self, item):
        pass

    def get(self):
        pass