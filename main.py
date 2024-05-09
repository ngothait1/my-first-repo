from Student import Student
from Employee import Employee

student = Student("Mike", 22, "Engineering", 1, 70)
print("This is from programmer 1, hi how are you, 123")
# student.foo()

print("This is from programmer 2")
employee = Employee("John", 40, "Software Engineer", 45000)
people = [student, employee]
for person in people:
    person.printMyself()









