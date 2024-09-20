class Person():
    def __init__(self,name) -> None:
        self.name = name

    def SayHi(self):
        print('Hi, my name is ', self.name)

p = Person('Igor') 
p.SayHi()  




