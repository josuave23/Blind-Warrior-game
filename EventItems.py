

class EventItems:
    def __init__(self, cost, description):
        self.cost = cost
        self.description = description
    
    def get_cost(self):
        return self.cost
    
    def get_description(self):
        print(self.description)