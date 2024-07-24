class CustomRange:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        else:
            current_value = self.current
            self.current += 1
            return current_value
        
for i in CustomRange(5):
    print(i)