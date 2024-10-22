

class Enemy:
    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name
        self.alive = True
    
    def get_health(self):
        return self.health
    def get_damage(self):
        return self.damage
    def get_name(self):
        return self.name
    def check_if_alive(self):
        return self.alive
    
    def set_health(self, x):
        self.health = x
    def set_damage(self, x):
        self.damage = x
    def set_name(self, x):
        self.name = x
    def swap_life(self, x):
        if self.alive == True:
            self.alive = False
        else:
            self.alive = True
        