class Student:
    def __init__(self,name,roll_number,marks):
        self.name =name
        self.roll_number = roll_number
        self.marks =marks
    def student_details(self):
        print(f"My Name is{self.name}")
        print(f"My roll_number is{self.roll_number}")
        print(f"My Marks  is{self.marks}")

    def passed(self):
        if self.marks>=40:
            print('pass')
        else:
            print("Failed")

student1 =Student("Venu",1,50)
student2 =Student("Kalyan",2,40)
student3 =Student("Myself",3,39)

student1.student_details()
student1.passed()

student3.student_details()
student3.passed()