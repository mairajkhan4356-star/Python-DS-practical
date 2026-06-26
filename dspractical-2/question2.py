print("~~~~~~~~~~~~~~~~Question 2: List Operations in Python~~~~~~~~~~~~~~~~")

print("a. Find the largest number in a list")
numbers =[90, 30, 67, 78,56 ]
print("largest numbers:",max(numbers))
print("======================================================")

print("b. Remove duplicates from a list")
dup_list = [2, 4, 5, 6, 7, 9, 5]
unique_list = list(set(dup_list))
print("List without duplicates:", unique_list)
print("======================================================")

print("c. Count how many even numbers are in a list")
even_list = [2, 4, 5, 6, 7, 7, 8]
even_count = sum(1 for x in even_list if x % 2 == 0)
print("Number of even elements:", even_count)
print("======================================================")

print("d. Input 5 numbers and store them in a list, then display")
user_list = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    user_list.append(num)
print("User-entered list:", user_list)
print("======================================================")

print("e. Function that returns the average of all numbers in a list")
def average(lst):
    return sum(lst) / len(lst) if lst else 0

print("Average of numbers:", average([10, 20, 30, 40, 50]))
print("======================================================")

print("f. Convert a string into a list of characters using list()")
my_string = "Python"
char_list = list(my_string)
print("List of characters:", char_list)
print("======================================================")

print("g. Join all elements of a list into a single string using join()")
words = ["Python", "is", "fun"]
joined_string = " ".join(words)
print("Joined string:", joined_string)