from random import *
class lottery:
    def __init__(self):
        self.up = 45
        self.down = 1
        self.number = []
        self.randNUM()
        self.max = int(input("Enter the max reward for the lottery: \n"))
    def randNUM(self):
        for i in range(6):
            self.number+=[randint(self.down,self.up)]

    #def getMax(self):
        #self.max = int(input("Enter the max reward for the lottery: \n"))

    def showNumber(self):
        print(f"{self.number}")

    def checkDigit(self, digit):
        if digit in self.number:
            index = self.number.index(digit)
            self.number.remove(self.number[index])
            return True
        else:
            return False

    def CorrectGuess(self,flag):
        count = 0
        if flag == True:
            count += 1
        return count




