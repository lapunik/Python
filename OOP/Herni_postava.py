import random
import time

random.seed(time.time())

class Postava:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.strengh = 30

    def introduce_yourself(self):
        print("Hi, Im " + self.name + " nice to meet you." )

    def health_state(self):
        print(self.name + ": [",end="")
        bar = int(10*(self.health/self.max_health))
        print(bar*"X",end="")
        print((10-bar)*" ",end="")
        print("] ",end="")
        print(str(self.health) + "/" + str(self.max_health))

    def protect(self, damage):
        print(self.name + " get: " + str(damage) + "dmg.")
        self.health -= damage
        if(self.health < 0):
            self.health = 0
        self.health_state()


    def strengh_up(self):
        excercise = 5
        self.strengh += excercise
        print(self.name + " increases his strength by: " + str(excercise) + "pt.")
        print("His strength is " + str(self.strengh) + "pt now.")        
        self.strengh += excercise

    def health_potion(self):
        health_increase = 10 + random.randint(0,5) 
        print(self.name + " use health potion: +" + str(health_increase) + "hp.")
        self.health += health_increase
        if(self.health > self.max_health):
            self.health = self.max_health
        self.health_state()
        self.health += health_increase

    def attack(self):
        damage = self.strengh + random.randint(-5,5) 
        print(self.name + " attack for: " + str(damage) + "dmg.")
        return damage
    
    def is_live(self):
        return self.health > 0 
    
    def celebrate(self):
        print(self.name + " is winnner!" )

def do_something(p1,p2):
    decision = random.randint(0,2)
    if(decision == 0):
        p2.protect(p1.attack()) 
    elif(decision == 1):
        p1.health_potion()
    elif(decision == 2): 
        p1.health_potion()

p1 = Postava("Legolas")
p2 = Postava("Goblin")

p1.introduce_yourself()
p2.introduce_yourself()

p1.health_state()
p2.health_state()

while(True):
    
    do_something(p1,p2)
    if not(p1.is_live()):
        print("Fight ends")
        p2.celebrate()
        break
    do_something(p2,p1)
    if not(p2.is_live()):
        print("Fight ends")
        p1.celebrate()
        break


