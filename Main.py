import Learning as lng
from random import choice
import pickle as pkl
class Main():
    def __init__(self):
        self.spezies = lng.Spezies()
    def learn(self):
        for i in range(lng.lng_vars.generations):
            print(i)
            self.spezies.evaluate()
            self.spezies.new_generation()
    def save(self):
        pkl.dump(self.spezies, open( "save.p", "wb" ))
    def load(self):
        self.spezies = pkl.load(open("save.p", "rb"))
    def show(self):
        self.spezies.index_one = 0
        self.spezies.index_two = 0
        while True:
            self.spezies.play_one_ball(choice([-1, 1]), show = True)
                
