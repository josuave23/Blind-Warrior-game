


class Items:
    def __init__(self, cost, damage, uses):
        self.cost = cost
        self.damage = damage
        self.uses = uses
        self.broken = False
    
    #Getters ------------------------

    #Get Cost
    def get_cost(self):
        return self.cost
    
    #get Damage
    def get_damage(self):
        return self.damage
    
    #get uses
    def get_uses(self):
        return self.uses
    

    #Setters --------------------------------
    
    #Set Cost
    def set_cost(self, x):
        self.cost = x

    #set damage
    def set_damage(self, x):
        self.damage = x
    
    #set uses
    def set_uses(self, x):
        self.uses = x
    
    #switch Broken
    def switch_broken(self):
        if self.broken == True:
            self.broken = False
        else:
            self.broken = True
        