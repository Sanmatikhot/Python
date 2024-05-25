class student:
        def __init__(self, name, rollno, division):
            self.name = name
            self.rollno = rollno
            self.division = division

        def __str__(self):
            return f"name:{self.name },rollno:{self.rollno},division:{self.division}"
s1 = student("sanmati", "25", "A")
s2 = student("sanika", "21", "B")
print(s1)
print(s2)
