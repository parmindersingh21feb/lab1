name = input("What is your name?")
birth_year = input("What is your year of birth?")

print(f"Hello, {name}")

from datetime import datetime
this_year = datetime.now().year

age = this_year - int(birth_year)

print(f"you must be {age} years old.")
