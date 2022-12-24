
# class Laptop:
#     def __init__(self):
#         print("Hello world")

#     def config(self):
#         print("Asus","i7", "1TB")

# laptop1 = Laptop()
# laptop2 = Laptop()

# # Laptop.config(laptop1)
# laptop1.config()
# laptop2.config()






# class Student:
#     def __init__(self,name,rollNo):
#         self.name = name
#         self.rollno = rollNo

#     def info(self):
#         print("name is : ", self.name, "roll number is : " , self.rollno)

# student1 = Student("Shivani", "65")
# student2 = Student("Upasana", "66")

# print(id(student1))
# print(id(student2))


# student1.info()
# student2.info()





# class Person:
#     def __init__(self):
#         self.name = "Ishan"
#         self.number = 32
    
#     def compare(self, other):
#         if(self.number == other.number):
#             return True
#         else:
#             return False


# p1 = Person()
# p2 = Person()
# p2.number = 18
# if p1.compare(p2):
#     print("same")
# else:
#     print("Different")
# print(p1.number)
# print(p2.number)






# class Car:
#     wheels = 4
#     #static variable
#     #Instance variables - value varies from obj to obj
#     def __init__(self):
#         self.company = "BMW"
#         self.mileage = 10

# car1 = Car()
# car2 = Car()

# Car.wheels = 5

# print(car1.mileage, car1.wheels)
# print(car2.mileage, car2.wheels)




class Student:

    collegeName = "LPU"

    def __init__(self, python, web, math):
        self.subject1 = python
        self.subject2 = web
        self.subject3 = math
    
    def avgCalculator(self):
        return (self.subject1 + self.subject2 + self.subject3)/3

    # def get_subject1(self):
    #     return self.subject1

    # def set_marks(self,value):
    #     self.subject1 = value

    #Below is a class method
    @classmethod
    def collegeDetail(cls):
        return cls.collegeName

student1 = Student(4,7,8)
student2 = Student(2,3,9)

print(student1.avgCalculator())

print(Student.collegeDetail())








class A:
    def __init__(self):
        print("Init of class A")

    def method1(self):
        print("This is method 1")
    
    def method2(self):
        print("This is method 2")

class B():
    def __init__(self):
        #super().__init__()
        print("Init of class B")
    def method3(self):
        print("This is method 3")

    def method4(self):
        print("This is method 4")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("Init of C")
    def method5(self):
        print("This is method 5")

obj = C()