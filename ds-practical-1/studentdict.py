

students = {}

print("~~~~~~~~~~~~~~~~Student Records~~~~~~~~~~~~~~~~~~~")
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks for {name}: "))
    students[name] = marks

print("\n--- Student Details ---")
for name, marks in students.items():
    print(f"Name: {name} | Marks: {marks}")
    
total_marks = sum(students.values())
average = total_marks / len(students)
print(f"\nClass Average: {average:.2f}")
highest_student = max(students, key=students.get)
print(f"Highest Marks Scored By: {highest_student} ({students[highest_student]} marks)")
