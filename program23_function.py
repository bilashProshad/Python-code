def message():
    print("This is message function")


def addition(num1, num2):
    print(num1 + num2)


def seriesAddition(m, n):
    sum = 0
    for i in range(m, n + 1, 1):
        sum += i
    return sum


message()
addition(10, 20)

add = seriesAddition(1, 100)
print(add)
