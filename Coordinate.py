import Learning as lng
from random import choice
import pickle as pkl
class Coordinate():
    def __init__(self):
        self.spezies = lng.Spezies()
    def learn(self):
        for i in range(lng.lng_vars.generations):
            print(i)
            dif = 0
            while dif <= lng.lng_vars.ahead:
                print("left player sucks")
                self.spezies.evaluate()
                dif = sum([x.fitness for x in self.spezies.population_one]) - sum([x.fitness for x in self.spezies.population_two])
                print(dif)
                self.spezies.new_generation()
            self.spezies.trainee = 1
            while dif >= -lng.lng_vars.ahead:
                print("right player sucks")
                self.spezies.evaluate()
                dif = sum([x.fitness for x in self.spezies.population_one]) - sum([x.fitness for x in self.spezies.population_two])
                print(dif)
                self.spezies.new_generation()
            self.spezies.trainee = 0
    def save(self):
        pkl.dump(self.spezies, open( "save.p", "wb" ))
    def load(self):
        self.spezies = pkl.load(open("save.p", "rb"))
    def show(self):
        self.spezies.index_one = 0
        self.spezies.index_two = 0
        while True:
            self.spezies.play_one_ball(choice([-1, 1]), show = True)
                

