class File:
    def __init__(self,name,size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"File name: {self.name}, File size: {self.size}"

    def __eq__(self, other):
        if self.name == other.name
