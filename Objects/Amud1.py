class Person:
    def __init__(self):
        self.age = None

    def show(self):
        print(f"name: {self.name}, age: {self.age}, kids: {self.kids}")

    def has_children(self):
        if self.kids() > 0:
            return True
        else:
            return False

    def age_group(self):
        if 0 <= self.age <= 18:
            return 'Child'
        elif 18 < self.age <= 60:
            return 'adult'
        elif 60 < self.age <= 120:
            return 'adult'


class Circle:
    pi = 3.14

    def area(self, radius):
        return (radius ** 2) * self.pi
    
    def circumference(self, radius):
        return 2 * self.pi * radius
