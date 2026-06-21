
print("~~~~~~~~~~~~~~~Squares from 1 to 10~~~~~~~~~~~~~~~~~~~~~~")
for i in range(1, 11):
    print(f"Square of {i} is: {i**2}")

print("--------- Squares from 1 to 10 ---------")
for i in range(1, 11):
    print(f"Square of {i} is: {i**2}")

print("\n--------- Even Number Counter ---------")
even_count = 0

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_count += 1

print("\nTotal even numbers you entered:", even_count)
print("~~~~~~~~~~~~~~~Even Number Counter~~~~~~~~~~~~~~~~~")
even_count = 0

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_count += 1

print("\nTotal even numbers you entered:", even_count)
