from Queue import Queue

graph = {
    "S": {"A": 2, "B": 1, "G": 9},
    "A": {"C": 2, "D": 3},
    "B": {"D": 2, "E": 4},
    "C": {"G": 4},
    "D": {"G": 4},
"E":{"E":0}
}

heuristicSLD={
    "S": 6,
    "A": 0,
    "B": 6,
    "C": 4,
    "D": 1,
    "E": 10,
    "G": 0,
}

class graphProblem:

    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return list(self.graph[state].keys())

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, cost_so_far, state1, action, state2):
        return cost_so_far + self.graph[state1][state2]


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self, graphProblem):
        return [self.child_node(graphProblem, action)
                for action in graphProblem.actions(self.state)]

    def child_node(self, graphProblem, action):
        next_state = graphProblem.result(self.state, action)
        #print("-- Path Cost: ", graphProblem.path_cost(self.path_cost, self.state, action, next_state))
        return Node(next_state, self, action,
                    graphProblem.path_cost(self.path_cost, self.state, action, next_state))

    def path(self):
        node, path_back = self, []

        while node:
            path_back.append(node)
            node = node.parent

        return list(reversed(path_back))

    def solution(self):
        return [node.action for node in self.path()[1:]]

def best_first_search(problem, f, pop_index=0):
    node = Node(problem.initial)
    if problem.goal_test(node.state): return node

    frontier = Queue(pop_index)
    frontier.sortEnQueue(node, f)
    explored = set()

    frontier.enQueue(node)

    while frontier:

        frontier.printQueue()
        node = frontier.deQueue()

        print("Parent: ", node.state,
              "Childs: ", [child.state for child in node.expand(problem)])

        if problem.goal_test(node.state): return node
        explored.add(node.state)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier: frontier.sortEnQueue(child, f)

    return None

def a_star(problem):
    return best_first_search(problem, lambda node: node.path_cost + heuristicSLD[node.state])

def gbfs(problem):
    return best_first_search(problem, lambda node: heuristicSLD[node.state])


graph_problem = graphProblem("S", "G", graph)

# A*
print("--------------A*--------------")
aStar = a_star(graph_problem)
print("Result:", aStar.solution())
print("Path Cost:", aStar.path_cost)

# GBFS

print("--------------GBFS--------------")
gbfs = gbfs(graph_problem)
print("Result:", gbfs.solution())
print("Path Cost:", gbfs.path_cost)
