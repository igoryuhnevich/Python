from abc import *


class SchoolMember(metaclass=ABCMeta):
    """представляет любого человека в школе"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(создан SchoolMember:{0})'.format(self.name))


@abstractmethod
def tell(self):
    """вывести информацию"""
    print('Имя: {0}  Возраст: {1}'.format(self.name,self.age),end=" ")


class Teacher(SchoolMember):
    """Представляет преподователя"""
    def __init__(self, name, age, salary):
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('(Зарплата "{0:d}")'.format(self.salary))


class Student(SchoolMember):
    """Представляет студента."""
    def __init__(self, name, age,marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student : {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки "{0:d}"'.format(self.marks))


t = Teacher('MR.Smith',40,20000)
s = Student('Jimm',21,2)  
# m = SchoolMember('Mr.fff',10)   - Error Abstract class

print()

members = [t,s]
for member in members:
    member.tell()    # работает как для преподователя так и для студента

             