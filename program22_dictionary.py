studentId = {
    "101": "Bilash Prosad",
    102 : "John"
}

print(studentId["101"])
print(studentId.get(102), "Invalid")
print(studentId.get(104))
print(studentId.get(105), "Not a valid key")
print(len(studentId))
print("-------------------")

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["colors"][0])
