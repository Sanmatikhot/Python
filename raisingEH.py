try:
    age = int(input("enter a number"))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(f" Error:{e}")
else:
    print("no error occurred.")
finally:
    print("finally block executed")
