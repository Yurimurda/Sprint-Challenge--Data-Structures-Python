class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        

    def append(self, item):
        self.data.append(item)
        

    def get(self):
        return self.data



buffer = RingBuffer(3)

buffer.get() 
    

