from classes.Calculator import Calculator

from utils import keys_to_string

calculator = Calculator()

keys = keys_to_string(calculator)

is_running = True

while is_running:
    user_choice = input(
        f"Type the name of an action that you wanna execute {keys}: ")

    try:
        first_value = float(input("Enter first value :\n"))
        second_value = float(input("Enter second value :\n"))

        result = calculator[user_choice](first_value, second_value)
        print(result)
    except:
        raise TypeError("There is incorrect value!\nTry again later !")