class Student : 
    college = "RC" 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"College : {Student.college}")    

s = Student("Towseef",23)
s.display()     

Student.college = "ABC"
print(Student.college)