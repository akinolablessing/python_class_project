class My_Set:
    
    def __init__(self):

        self.my_set = set()

    def is_Empthy(self)->bool:
        if len(self.my_set) == 0:
            return True

    def isFull(self):
        if len(self.my_set) == 0:
            return False


    def add(self, element):
        return self.my_set.add(element)

    def addElement(self, element):
        return self.my_set.add(element)

    def getElement(self):
        return self.my_set

    def update(self, new_element):
        return self.my_set.update(new_element)

    def intersection(self, new_element):
        if self.my_set == new_element:
          return new_element

    #def getIntersection(self):
       # return self.my_set











