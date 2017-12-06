import random 


class Agent():
    def __init__(self,environment, agents, x = None, y = None):
        #self.y = 0
        #self.x = None
        if (x == None):
            self.x = random.randint(0,299)
        else:
            self.x = x
        
        if (y == None):
            self.y = random.randint(0,299)
        else:
            self.y = y
        
        self.agents = agents
        self.randomize()
        self.environment = environment
        self.store = 0 
        
        
    def eat(self): 
     if self.environment[self.y][self.x] > 10:
         self.environment[self.y][self.x] -= 10
         self.store += 10 
         
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5       
    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent) 
            if distance <= neighbourhood:
                sum = self.store + agent.store
                b = sum/2  #the average
                self.store = b
                agent.store = b
               # print("sharing " + str(distance) + " " + str(b))
        
 
    def randomize(self):
        self.y = random.randint(0,299)
        self.x = random.randint(0,299)


    def move(self):

        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300


