

class Specials:
    def __init__(self, effect, uses):
        self.effect = effect
        self.uses = uses


    #get uses
    def get_uses(self):
        return self.uses
    
    #get effect
    def get_effect(self):
        return self.effect

    #set uses
    def set_uses(self, x):
        self.uses = x

    #set effect (user set)
    def set_effect(self, x):
        self.effect = x