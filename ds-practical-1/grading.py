
print("~~~~~~~~~~~~~~~~~~Grading System~~~~~~~~~~~~~~~~")
marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75 and marks <= 89:
    grade = "B"
elif marks >= 50 and marks <= 74:
    grade = "C"
else:
    grade = "Fail"

print("Your Grade is:", grade)
print("~~~~~~~~~~~~~~~~~Thank You~~~~~~~~~~~~~~~")
