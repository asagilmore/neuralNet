
class network:
    def __init__(self):
        self.layers = []
        self.cost = None
        self.cost_derivative = None
    def add(self,layer):
        self.layers.append(Layer)
    
    def setCost(self,cost,cost_derivative):
        self.cost = cost
        self.cost_derivative = cost_derivative

    def 