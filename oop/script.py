class Person :
    def __init__(self, name,age,gender):
        self.name= name
        self.age=int(age)
        self.gender= gender

    def introduce(self):
        print (f'Hi, my name is {self.name}, I am {self.age} years old.')
    
    def get_age(self):
        return self.age

    def isAdult(self):
        return self.age > 18
         
        
class Student(Person) :
    def __init__(self,name, age, gender, student_id ):
        super().__init__(name,age,gender)
        self.student_id=student_id
    
    def introduce(self):
         print(f"Hi, I’m {self.name}, a student with ID {self.student_id}, and I am {self.get_age()} years old.")

    def study(self):
        print(f"{self.name} is studying.")

    @classmethod
    def from_person(cls,person,student_id):
        return cls(person.name,person.age,person.gender,student_id)

person1 = Person("Great" , 20, "male")

person1.introduce()
print("Is adult?", person1.isAdult())

student1 = Student("Alice", 19, "Female", "S12345")
student1.introduce()
student1.study()

student2= Student(person1.name, person1.age,person1.gender,"23wer3")
student2.introduce()
student2.study()

student3=Student.from_person(person1,"e9ej84")
student2.introduce()
student2.study()
