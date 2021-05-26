puzzle=[[7,1,2],[7,10000,4],[8,3,6]]
# puzzle=[[6,1,10,2],[7,11,4,14],[5,10000,9,15],[8,12,13,3]]
# puzzle=[[13,10,11,6],[5,7,4,8],[1,12,14,9],[3,15,2,10000]]

def returnParameters(puzzle):
    # CREATUG FLAT PUZZLE
    flatPuzzle = [col for row in puzzle for col in row]

    # FINDING DIMENSION
    dimension = len(flatPuzzle)

    # COUNTING INVERSION
    inversion = 0
    for i in range(dimension):
        count = 0
        for j in range(i + 1, dimension):
            if (flatPuzzle[i] > flatPuzzle[j]):
                if (flatPuzzle[i] == 10000): continue
                count = count + 1
        # print(count)
        inversion = inversion + count

    # FINDING BLANK TILES POSITION
    ##    blanktilePosition=0
    for row in puzzle:
        for col in row:
            if (col == 10000):
                blanktilePosition = len(puzzle) - puzzle.index(row)

    return dimension, inversion, blanktilePosition


dimension, inversion, blanktilePosition = returnParameters(puzzle)

print("Dimension: ", dimension, "\nTotal Inversion: ", inversion, "\nBlank Tiles Position from Bottom: ",
      blanktilePosition)


def isEven(value):
    if (value % 2) == 0:
        return True
    else:
        return False


def solvability(dimension, inversion, blanktilePosition):
    solvable = False

    if not isEven(dimension) and isEven(inversion):
        solvable = True

    elif isEven(dimension) and not isEven(blanktilePosition) and isEven(inversion):
        solvable = True

    elif isEven(dimension) and isEven(blanktilePosition) and not isEven(inversion):
        solvable = True

    return solvable


print("\n\nIs Solvable: ", solvability(dimension, inversion, blanktilePosition))
