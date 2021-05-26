# Set cant be access with index number
# set can be created with {} or set()
# set do not show duplicate number

num1 = {1, 2, 3, 4, 5, 5}
num2 = set([2, 4, 4, 6, 8, 10])
num3 = [11, 15, 16, 13, 20]
num3 = set(num3)

print(num1)
print(num3)

print(num1 | num2) # union
print(num1 & num2) # intersection
print(num1 - num2)
