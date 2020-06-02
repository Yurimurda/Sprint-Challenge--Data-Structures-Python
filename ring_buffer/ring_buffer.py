class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        self.current = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.current] = item 
            self.current += 1  

            if len(self.data) == self.current:
                self.current = 0
        

        

    def get(self):
        return self.data



buffer = RingBuffer(3)

buffer.get() 
    

