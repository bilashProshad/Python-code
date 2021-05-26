books = []
books.append("C")
books.append("C++")
books.append("Java")
books.append("Python")
print(books)
print(books[-1]) # print top
books.pop()
print(books[-1])
books.pop()
books.pop()
books.pop()
#books.pop()
if not books:
    print("Stack is empty")
