class Add:
    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print ("First"+ str(self.first))
        print ("Second"+ str(self.second))
        print ("Add" + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second
         

object = Add(10,20)

object.calculate()
object.display()
