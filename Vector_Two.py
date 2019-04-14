import pygame
from random import uniform
class Vector_Two():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, other):
        self.x += other.x
        self.y += other.y
    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
    def small_change(self, change_size):
        self.x += uniform(-change_size, change_size)
        self.y += uniform(-change_size, change_size)
