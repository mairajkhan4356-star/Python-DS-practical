print("~~~~~~~~~~~~~~~~~~~~Question 1: Tuple Operations in Python~~~~~~~~~~~~~~~~~~~~~~~")

print("a. Create a tuple with 5 different elements and print it")
my_tuple = (30, "Mairaj", 6.78, True, [1, 2, 3])
print("Tuple:", my_tuple)
print("======================================================")

print("b. Access the first and last elements of a tuple using indexing")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("======================================================")

print("c. Slice a tuple and print the middle 3 elements")
slice_tuple = (3, 5, 8, 9, 4, 1, 2)
print("Middle 3 elements:", slice_tuple[2:5])
print("======================================================")

print("d. Concatenate two tuples and print the result")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Concatenated tuple:", tuple1 + tuple2)
print("======================================================")

print("e. Reverse a tuple using slicing")
print("Reversed tuple:", tuple1[::-1])
print("======================================================")

print("f. Count how many times an element appears in a tuple")
count_tuple = (3, 2, 6, 7, 4, 9, 5)
print("Count of 2:", count_tuple.count(2))
print("======================================================")

print("g. Find the index of a specific element in a tuple")
print("Index of 3:", count_tuple.index(3))
print("======================================================")

print("h. Check if an element exists in a tuple")
element = 4
print(f"Does {element} exist?", element in count_tuple)
print("======================================================")

print("i. Convert a list to a tuple")
my_list = [10, 20, 30, 40]
converted_tuple = tuple(my_list)