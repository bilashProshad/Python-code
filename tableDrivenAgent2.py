import random


class Object:
    def __repr__(self):
        return '<%s>' % getattr(self, '__name__', self.__class__.__name__)


class Agent(Object):
    def __init__(self):
        def program(percept): abstract

        self.program = program


loc_A, loc_B, loc_C, loc_D = 'A', 'B', 'C', 'D'


class vaccumEnvironment():

    def __init__(self):
        self.status = {loc_A: random.choice(['Clean', 'Dirty']),
                       loc_B: random.choice(['Clean', 'Dirty']),
                       loc_C: random.choice(['Clean', 'Dirty']),
                       loc_D: random.choice(['Clean', 'Dirty'])
                       }

    def add_object(self, object, location=None):
        object.location = location or self.default_location(object)
        #print("Object location: ", object.location)

    def default_location(self, object):
        return random.choice([loc_A, loc_B, loc_C, loc_D])
        '''
        if object.location == loc_A:
            return random.choice([loc_B, loc_C])
        elif object.location == loc_B:
            return random.choice([loc_A, loc_D])
        elif object.location == loc_C:
            return random.choice([loc_A, loc_D])
        elif object.location == loc_D:
            return random.choice([loc_C, loc_B])
        '''

    def percept(self, agent):
        #print("Agent Location: ", agent.location)
        #print("Agent Status: ", self.status[agent.location])
        return (agent.location, self.status[agent.location])

    def execute_action(self, agent, action):
        if agent.location == loc_A:
            if action == 'Right':
                agent.location = loc_B
            elif action == 'Down':
                agent.location = loc_C

        elif agent.location == loc_B:
            if action == 'Left':
                agent.location = loc_A
            elif action == 'Down':
                agent.location = loc_D

        elif agent.location == loc_C:
            if action == 'Right':
                agent.location = loc_D
            elif action == 'Up':
                agent.location = loc_A

        elif agent.location == loc_D:
            if action == 'Left':
                agent.location = loc_C
            elif action == 'Up':
                agent.location = loc_B

        elif action == 'Suck':
            # if self.status[agent.location]=='Dirty'
            self.status[agent.location] = 'Clean'


class tableDrivenAgent(Agent):

    def __init__(self, table):
        Agent.__init__(self)
        percepts = []

        def program(percept):
            percepts.append(percept)
            print(percepts)
            action = table.get(tuple(percepts))
            print('Agent perceives ', percept, ' and does ', action)
            return action

        self.program = program


def tableDrivenVaccumAgent():
    table = {
        ((loc_A, 'Clean'),): 'Right',
        ((loc_A, 'Clean'),): 'Down',
        ((loc_A, 'Dirty'),): 'Suck',
        ((loc_B, 'Clean'),): 'Left',
        ((loc_B, 'Clean'),): 'Down',
        ((loc_B, 'Dirty'),): 'Suck',
        ((loc_C, 'Clean'),): 'Up',
        ((loc_C, 'Clean'),): 'Right',
        ((loc_C, 'Dirty'),): 'Suck',
        ((loc_D, 'Clean'),): 'Left',
        ((loc_D, 'Clean'),): 'Up',
        ((loc_D, 'Dirty'),): 'Suck',

        ((loc_A, 'Clean'), (loc_A, 'Clean')): 'Down',
        ((loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
        ((loc_A, 'Clean'), (loc_B, 'Clean')): 'Left',
        ((loc_A, 'Clean'), (loc_C, 'Clean')): 'Up',
        ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
        ((loc_A, 'Clean'), (loc_C, 'Dirty')): 'Suck',
        ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',

        ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
        ((loc_A, 'Dirty'), (loc_B, 'Clean')): 'Left',
        ((loc_A, 'Dirty'), (loc_C, 'Clean')): 'Up',
        ((loc_A, 'Dirty'), (loc_B, 'Dirty')): 'Right',
        ((loc_A, 'Dirty'), (loc_C, 'Dirty')): 'Down',
        ((loc_A, 'Dirty'), (loc_A, 'Dirty')): 'Suck',

        ((loc_B, 'Clean'), (loc_A, 'Clean')): 'Right',
        ((loc_B, 'Clean'), (loc_B, 'Clean')): 'Down',
        ((loc_B, 'Clean'), (loc_B, 'Clean')): 'Left',
        ((loc_B, 'Clean'), (loc_D, 'Clean')): 'Up',
        ((loc_B, 'Clean'), (loc_D, 'Clean')): 'Left',
        ((loc_B, 'Clean'), (loc_B, 'Dirty')): 'Right',
        ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
        ((loc_B, 'Clean'), (loc_D, 'Dirty')): 'Suck',

        ((loc_B, 'Dirty'), (loc_A, 'Clean')): 'Right',
        ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
        ((loc_B, 'Dirty'), (loc_B, 'Dirty')): 'Right',

        ((loc_C, 'Dirty'), (loc_C, 'Dirty')): 'Suck',
        ((loc_C, 'Clean'), (loc_C, 'Dirty')): 'Suck',
        ((loc_C, 'Clean'), (loc_D, 'Dirty')): 'Suck',
        ((loc_C, 'Clean'), (loc_C, 'Clean')): 'Up',
        ((loc_C, 'Clean'), (loc_C, 'Clean')): 'Right',

        ((loc_D, 'Clean'), (loc_B, 'Dirty')): 'Suck',
        ((loc_D, 'Clean'), (loc_B, 'Clean')): 'Down',
        ((loc_D, 'Clean'), (loc_B, 'Clean')): 'Left',
        ((loc_D, 'Clean'), (loc_B, 'Clean')): 'Down',
        ((loc_D, 'Clean'), (loc_B, 'Clean')): 'Left',
        ((loc_D, 'Clean'), (loc_D, 'Dirty')): 'Suck',
        ((loc_D, 'Clean'), (loc_D, 'Clean')): 'Up',
        ((loc_D, 'Clean'), (loc_D, 'Clean')): 'Left',
        ((loc_D, 'Dirty'), (loc_D, 'Dirty')): 'Suck',


        ((loc_C, 'Clean'), (loc_D, 'Clean')): 'Right',
        ((loc_C, 'Clean'), (loc_D, 'Clean')): 'Up',

        ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
        ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',

        ((loc_A, 'Clean'), (loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
        ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
        ((loc_A, 'Dirty'), (loc_A, 'Dirty'), (loc_A, 'Dirty')): 'Suck',

    }
    return tableDrivenAgent(table)




Tagent = tableDrivenVaccumAgent()
env = vaccumEnvironment()
env.add_object(Tagent)

for _ in range(10):
    percept = env.percept(Tagent)
    #print("Percept: ", percept)
    action = Tagent.program(percept)
    #print("Action: ",action)
    env.execute_action(Tagent, action)


