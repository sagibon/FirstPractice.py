class Person:
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

class Course:

    def write(self):
        print(f"course number: {self.number}. course name: {self.name}. number enrolled: {self.enrolled}. max: {self.max}")

    def avail(self):
        return self.max-self.enrolled

    def newstudents(self, newones):
        if self.enrolled < self.max:
            self.enrolled += newones

        elif self.enrolled == self.max:
            print("Course is full!")

        else:
            print("error")


class HardDisk():
    def __init__(self,space):
        self.space = space
        self.usedspace = 0
        self.numoffiles = 0

    def write(self):
        print(f"hard disk size: {self.space} used space: {self.usedspace}, number of files {self.numoffiles} ,free space: {self.freeSpace()}")

    def freeSpace(self):
        return self.space-self.usedspace

    def addFile(self, sizeadd):
        if self.usedspace + sizeadd <= self.space:
            self.usedspace+= sizeadd
            self.numoffiles+=1
            return True
        else:
            print("Cant add file, memory full")
            return False

    def delFile(self, sizedel):
            self.usedspace -= sizedel
            self.numoffiles -= 1
            if self.usedspace < 0:
                self.usedspace = 0
            if self.numoffiles < 0:
                self.numoffiles = 0


