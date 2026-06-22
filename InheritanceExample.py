class person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
        
    def display(self):
        print(f"Name : {self.name}")    
        print(f"Age : {self.age}")

class Employee(person):
    def __init__(self,name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def display(self):
        super().display()
        print(f"Salary : {self.salary}")         

e = Employee("Towseef,",23,25000)
e.display()        