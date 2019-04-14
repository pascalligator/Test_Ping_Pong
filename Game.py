import Player as ply
import Game_Vars as vars
import pygame
class Game():
    def __init__(self):
        self.player_one = ply.Player(vars.data_player_one)
        self.player_two = ply.Player(vars.data_player_two)
        self.ball = ply.Player(vars.data_ball)
        self.bounds_left = ply.Player(vars.data_bounds_left)
        self.bounds_right = ply.Player(vars.data_bounds_right)
        self.bounds_top = ply.Player(vars.data_bounds_top)
        self.bounds_bottom = ply.Player(vars.data_bounds_bottom)
        self.drawables = [self.player_one, self.player_two, self.ball]
    def update(self):
        self.player_one.update()
        self.player_two.update()
        self.ball.update()
    def collision(self):
        objects = [self.player_two, self.bounds_left, self.bounds_right, self.bounds_top, self.bounds_bottom]
        self.player_one.collision(objects, vars.change_size)
        objects = [self.player_one, self.bounds_left, self.bounds_right, self.bounds_top, self.bounds_bottom]
        self.player_two.collision(objects, vars.change_size)
        objects = [self.player_one, self.player_two, self.bounds_left, self.bounds_right, self.bounds_top, self.bounds_bottom]
        return self.ball.collision(objects, vars.change_size)
    def draw(self):
        for object in self.drawables:
            pygame.draw.rect(self.screen, object.color, (object.pos.x, object.pos.y, object.size.x, object.size.y), 0)
    def clear(self):
        self.screen.fill((0,0,0))
    def flip(self):
        pygame.display.flip()
    def get_inputs(self):
        inputs = []
        inputs.append((self.player_one.pos.x + self.player_one.size.x / 2) / vars.width)
        inputs.append((self.player_one.pos.y + self.player_one.size.y / 2) / vars.height)
        inputs.append(self.player_one.vel.x / self.player_one.max_vel.x)
        inputs.append(self.player_one.vel.y / self.player_one.max_vel.y)
        inputs.append((self.player_two.pos.x + self.player_two.size.x / 2) / vars.width)
        inputs.append((self.player_two.pos.y + self.player_two.size.y / 2) / vars.height)
        inputs.append(self.player_two.vel.x / self.player_two.max_vel.x)
        inputs.append(self.player_two.vel.y / self.player_two.max_vel.y)
        inputs.append((self.ball.pos.x + self.ball.size.x / 2) / vars.width)
        inputs.append((self.ball.pos.y + self.ball.size.y / 2) / vars.height)
        inputs.append(self.ball.vel.x / self.ball.max_vel.x)
        inputs.append(self.ball.vel.y / self.ball.max_vel.y)
        return inputs
    def convert_outputs(self, outputs_one, outputs_two):
        if outputs_one.index(max(outputs_one)) == 0:
            self.player_one.vel.y = -self.player_one.max_vel.y
        elif outputs_one.index(max(outputs_one)) == 1:
            self.player_one.vel.y = 0
        else:
            self.player_one.vel.y = self.player_one.max_vel.y
        if outputs_two.index(max(outputs_two)) == 0:
            self.player_two.vel.y = -self.player_two.max_vel.y
        elif outputs_two.index(max(outputs_two)) == 1:
            self.player_two.vel.y = 0
        else:
            self.player_two.vel.y = self.player_two.max_vel.y
    def setup_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((vars.width, vars.height))
