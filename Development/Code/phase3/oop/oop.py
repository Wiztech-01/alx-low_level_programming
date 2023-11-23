# studentName = "Lynn"

# def studentOneLearn():
#     print("Learning")
    
# studentOneLearn()

class Student:
    # the init method runs every time thete is a new instance
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #    print(f"{name} with {age} created")
           
    def learn(self):
        print(f"{self.name} Going through canvas")
    
    def research(self, topic):
        print(f"{self.name} researching {topic}")

# stud1 = Student()
# print(stud1.learn())
# stud2 = Student()

# stud1.learn()
# stud2.learn()
# stud2.research("Big O notation")

stud1 = Student ("Brian" , 24)
stud2 = Student ("Joyce", 23)

print(stud1.name, stud1.age)
print(stud2.name, stud2.age)

stud1.learn()
stud1.research("oop")
stud2.research("Advantages of social media")
