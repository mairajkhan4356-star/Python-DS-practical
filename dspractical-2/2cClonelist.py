print("~~~~~~~~~~~~2c. Copy or clone a list in Python~~~~~~~~~~~~~")

original_list = [1, 2, 3, 4, 5]


copy_list1 = original_list[:]
print("Copy using slicing:", copy_list1)


copy_list2 = list(original_list)
print("Copy using list():", copy_list2)


copy_list3 = original_list.copy()
print("Copy using copy():", copy_list3)

# Method 4: Using deepcopy (for nested lists)
import copy
nested_list = [[1, 2], [3, 4]]
deep_copy_list = copy.deepcopy(nested_list)
print("Deep copy of nested list:", deep_copy_list)