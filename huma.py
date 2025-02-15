from random import randrange

from huma import Human
from human import Human


class Native(Human):
    def __init__(self, name,date_of_birth,gender,height,phone):
        super().__init__(name,date_of_birth,gender,height)
        self.phone = phone
        self._id = self.generate_id()

    @staticmethod
    def generate_id():
        return "scv"+str(randrange(1000,9999))

    def __str__(self):
        return f'''
        {super().__str__()}
        {self.phone}
        {self._id}
         '''

    n1 = Native("Ayomide","12-2-2005","female",5.6,"091553098765")
    print(n1)
