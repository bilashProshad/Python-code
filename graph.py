romaniaMap = {
    "Arad": {"Timisoara": 118, "Sibiu": 140, "Zerind": 75},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu": 80},
    "Sibiu": {"Arad": 140, "Oradea": 151, "RimnicuVilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}

initial_state, goal_state = "Arad", "Bucharest"
frontier = []
explored = set()
path = list()


def goal(state):
    return state == goal_state



def graphSearch(romaniaMap):
    frontier.append(initial_state)

    while True:
        if len(frontier)==0:
            print("Not found")
            return

        result = frontier.pop()
        path.append(result)
        if goal(result):
            print("success")
            break
        else:
            actions = list(romaniaMap[result].keys())
            for i in actions:
                if i not in explored or i not in frontier:
                    frontier.append(i)


    #return solution


graphSearch(romaniaMap)
print(path)

'''
frontier.append("Arad")
result = frontier.pop()
actions = list(romaniaMap[result].keys())
explored.add(result)
# print(actions)
for i in actions:
    frontier.append(i)
# print(frontier)
result = frontier.pop()
# print(result)
actions = list(romaniaMap[result].keys())
for i in actions:
    if i not in explored or i not in frontier:
        frontier.append(i)

result = frontier.pop()
#print(result)

actions = list(romaniaMap[result].keys())
for i in actions:
    if i not in explored or i not in frontier:
        frontier.append(i)

result = frontier.pop()
print(result)

print("-------------------")
print(romaniaMap["Arad"].keys())
'''