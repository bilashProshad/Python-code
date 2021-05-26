noOfQueen = 4


def configureNQueens(noOfQueen, domain=[], variables=[]):
    variables = [-1] * noOfQueen
    return noOfQueen, domain, variables


def addDomain(n, Q, domain):
    for i in range(n):
        Q[i] = domain
    return Q


def setBoard(domain):
    n, domain, variables = configureNQueens(noOfQueen, domain)
    variables = addDomain(n, variables, domain)
    return n, domain, variables


def removeAttacks(row, column, variables):
    variables[row] = column
    i, j = row, column

    for k in range(len(variables)):
        if type(variables[k]) == list:
            if column in variables[k]: variables[k].remove(column)

            for l in variables[k]:
                if abs(j - 1) == abs(k - i):
                    vList = list(variables[k])
                    vList.remove(l)
                    variables[k] = vList

            if len(variables[k]) == 0:
                print("No possible solution")
                continue
    print(variables)
    return variables


def placeInitialQueen(inRow, domain, variables, qPlaced):
    for column in domain:
        n, domain, variables = setBoard(domain=[i for i in range(noOfQueen)])
        variables = removeAttacks(inRow, column, variables)
        qPlaced.append(variables)

    return inRow, qPlaced


def placeRestQueens(n, inRow, qPlaced):
    firstQueen = 0
    q = qPlaced[inRow]
    qc = qPlaced[inRow][0]

    print("After Placing Queen ", firstQueen, "in Column: ", qc)

    for i in range(1, n):
        column = q[firstQueen + i]
        print(column)
        for c in column:
            print("Placing Queen ", firstQueen + i, "in Column: ", c)
            q = removeAttacks(firstQueen + i, c, q)
    return q


def placeNextQueen(q, nextQueenNo):
    for i in range(1, n):
        nextQueenNo = i
        columns = q[nextQueenNo]

        for c in columns:
            print("Placing Queen ", nextQueenNo, "in column: ", c)
            q = removeAttacks(i, c, q)

    return q, nextQueenNo


qPlaced = []
n, domain, variables = setBoard(domain=[i for i in range(noOfQueen)])
nextQueenNo, qPlaced = placeInitialQueen(0, domain, variables, qPlaced)

for i in range(n):
    q = qPlaced[i]
    placeNextQueen(q, nextQueenNo)
