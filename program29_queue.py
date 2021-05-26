from collections import deque

bank = deque(["A", "B", "C", "D"])
bank.append("E")
print(bank)
bank.popleft()
bank.popleft()
print(bank)
