def swap_elements(lst, index1, index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp
    print("Updated list:", lst)

my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)
swap_elements(my_list, 1, 3)
