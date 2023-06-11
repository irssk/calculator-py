# Inheritance
# Abstract
class Human:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def greeting(self):
        print("Hello world")


# Encapsulation
class Employee(Human):
    status = "unemployed"

    def __init__(self, outter_name: str, outter_surname: str, outter_age: int, outter_income: str):
        super().__init__(outter_name, outter_surname, outter_age)

        self.income = outter_income
        self.status = "full-time"

    def fine(self, sum_of_fine):
        self.income = int(self.income[1:]) - sum_of_fine

    def greeting(self):
        return print("Hello , unemployed humination!")


emp_instance = Employee("John", "Doe", 23, "$3000")
hum_instance = Human("John", "Doe", 23)

hum_instance.greeting()
emp_instance.greeting()

emp_instance.fine(200)
print(emp_instance.__dict__)