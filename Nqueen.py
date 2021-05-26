n = 4
Q = [0] * n

def PlaceQueen(Q, r):
    if (r == n):
        print(Q)

    else:
        for j in range(n):
            legal = True
            for i in range(r):
                if ((Q[i] == j) or (Q[i] == j + r - i) or ((Q[i] == j - r + i))):
                    legal = False

            if legal:
                Q[r] = j
                PlaceQueen(Q, r + 1)


PlaceQueen(Q, 0)