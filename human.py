from datetime import datetime


class Human:
    def __init__(self, name, date_of_birth,gender,height):
        self._name = name
        self._date_of_birth = date_of_birth
        self._age = self.get_age
        self._gender = gender
        self._height = height


def get_age(self):
    day, month, year = self._date_of_birth.split('-')
    current_year = datetime.now().year
    return current_year - int(year)

def __str__(self):
    return f'''
    Name: {self._name}
    Age: {self.get_age()}
    Gender: {self._gender}
    Height: {self._height}
    '''
