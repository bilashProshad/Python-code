numbers = input("Enter numbers for addition: ")
list = numbers.split()

sum = 0
for num in list:
    sum += int(num)
print(sum)