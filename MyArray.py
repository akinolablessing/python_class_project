class MyArray:

    def __init__(self,size):
        self.size = size
        self.capacity = size
        self.my_array = [] * size

    def is_empty(self):
        return self.size == 0

first_array = MyArray(5)
first_array.is_empty()