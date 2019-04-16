import Game as gm
import Network as nw
import Learning_Vars as lng_vars
import Keys as ks
from time import sleep
from random import uniform
class Spezies():
    def __init__(self):
        self.population_one = [nw.Network() for i in range(lng_vars.population_size)]
        self.population_two = [nw.Network() for i in range(lng_vars.population_size)]
        self.both_populations = [self.population_one, self.population_two]
        self.index_one = 0
        self.index_two = 0
        self.trainee = 0
    def evaluate(self):
        for i in range(2):
            for j in range(len(self.both_populations[i])):
                for l in range(len(self.both_populations[1 - i])):
                    self.index_one = j
                    self.index_two = l
                    self.play_one_ball(ball_start_direction = i * 2 - 1, show = False)
    def play_one_ball(self, ball_start_direction, show = False):
        game = gm.Game()
        if show == True:
            game.setup_pygame()
        game.ball.vel.x = game.ball.max_vel.x * ball_start_direction
        game.ball.vel.y = uniform(-game.ball.max_vel.y, game.ball.max_vel.y)
        while game.ball.vel.y < 0.1 and game.ball.vel.y > -0.1:
            game.ball.vel.y = uniform(-game.ball.max_vel.y, game.ball.max_vel.y)
        fail_alarm = 0
        play = True
        while play == True:
            game.convert_outputs(self.population_one[self.index_one].feedforward(game.get_inputs()), \
                self.population_two[self.index_two].feedforward(game.get_inputs()))
            game.update()
            collisions = game.collision()
            if collisions == True:
                self.population_one[self.index_one].fitness += 1
                break
            elif collisions == False:
                self.population_two[self.index_two].fitness += 1
                break
            if show == True:
                keys = ks.keys()
                self.index_one += keys[0]
                self.index_two += keys[1]
                print(self.index_one, self.index_two)
                game.clear()
                game.draw()
                game.flip()
                sleep(0.025)
            fail_alarm += 1
            if fail_alarm > 3000:
                print("fail alarm")
                break
    def new_generation(self):
        self.population_one.sort(key = lambda x: x.fitness, reverse = True)
        self.population_two.sort(key = lambda x: x.fitness, reverse = True)
        for j in range(lng_vars.mutated_copies):
            self.both_populations[self.trainee][lng_vars.true_copies + j].mutate()
        del self.both_populations[self.trainee][len(self.both_populations[self.trainee]) - lng_vars.added_randoms : ]
        for j in range(lng_vars.added_randoms):
            self.both_populations[self.trainee].append(nw.Network())
        for i in range(2):
            for j in range(len(self.both_populations[i])):
                self.both_populations[i][j].fitness = 0
        