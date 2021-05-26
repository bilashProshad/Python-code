graph = {
    "S": {"A": 2, "B": 1, "G": 9},
    "A": {"C": 2, "D": 3},
    "B": {"D": 2, "E": 4},
    "C": {"G": 4},
    "D": {"G": 4},
    "E": {"E": 0}
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

class Queue:
    def __init__(self, pop_index):
        self.queue = []
        self.pop_index = pop_index
    def append(self, item):
        self.queue.append(item)
    def sortAppend(self, item, f):
        self.queue.append(item)
        self.queue.sort(key=f)
    def extend(self, items):
        self.queue.extend(items)
    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(self.pop_index)
        else:
            raise Exception('FIFOQueue is empty')
    def printQueue(self):
        def __len__(self):
            return len(self.queue)
    def __contains__(self, item):
        return item in self.queue

def best_first_search(problem, f, pop_index=0):
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return state
    frontier = Queue(pop_index)
    frontier.sortAppend(node, f)
    explored = set()
    while frontier:
        frontier.printQueue()
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.sortAppend(child, f)
    return None


print("--------------UCS------------------")
graph_problem=graphProblem("S", "G", graph)
ucs  =best_first_search(graph_problem, lambda node:node.path_cost)
print("Traveling routes:",ucs.solution())
print(" Total Path cost :",ucs.path_cost)
