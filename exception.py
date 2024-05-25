try:
    result = 10/0
except ZeroDivisionError  as e:
    print(f"Error: Division by zero -{e}")
else:
    print("no error occurred.")
finally:
    print("finally block executed")

