numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter your text: ")

for i in text:
    i.lower()
    if i >= 'a' and i <= 'z':
        numOfLetters += 1
    elif i >= '0' and i <= '9':
        numOfDigits += 1
    elif i == ' ':
        numOfWords += 1

print("Num of words:", numOfWords+1)
print("Num of letters:", numOfLetters)
print("Num of digits:", numOfDigits)
