class MyArray:

    def __init__(self,size):
        self.size = 0
        self.capacity = size
        #self.my_array = [] * size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return len(self.size) == self.capacity
