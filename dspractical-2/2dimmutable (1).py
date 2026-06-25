print("~~~~~~~~~~~2d. Check immutability property of Python tuples~~~~~~~~~~~~")


immutable_tuple = (10, 20, 30)

print("Original tuple:", immutable_tuple)

# Try to modify an element
try:
    immutable_tuple[0] = 99
except TypeError as e:
    print("Error (immutability check):", e)
