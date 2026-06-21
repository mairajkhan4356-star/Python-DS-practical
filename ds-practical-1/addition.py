print("---------Addition-------")
user_input = input("Enter numbers separated by spaces: ")
numbers = [float(num) for num in user_input.split()]
total = sum(numbers)
print("The total sum is:", total)
