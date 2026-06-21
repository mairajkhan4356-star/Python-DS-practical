list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
print("original list:", list)

max = max(list)
min = min(list)
aver = sum(list) / len(list)
asce = sorted(list)
desc = sorted(list, reverse=True)

print(max)
print(min)
print(aver)
print(asce)
print(desc)
