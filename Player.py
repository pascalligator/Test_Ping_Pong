import Vector_Two as v
class Player():
    def __init__(self, data):
        self.pos = v.Vector_Two(data[0], data[1])
        self.vel = v.Vector_Two(data[4], data[5])
        self.size = v.Vector_Two(data[2], data[3])
        self.max_vel = v.Vector_Two(data[6], data[7])
        self.name = data[8]
        self.color = data[9]
    def update(self):
        self.pos.add(self.vel)
    def collision(self, others, change_size):
        for other in others:
            if self.overlap(other) == True:
                self.pos.sub(self.vel)
                if self.name == "ball":
                    if other.name == "player":
                        self.vel.x *= -1
                        self.update()
                        if self.overlap(other) == True:
                            self.vel.y *= -1
                            self.update()
                    elif other.name == "bound_top_bottom":
                        self.vel.y *= -1
                    elif other.name == "bound_left":
                        return False
                    else:
                        return True
                    self.vel.small_change(change_size)
    def overlap(self, other):
        if self.pos.x < other.pos.x + other.size.x and self.pos.x + self.size.x > other.pos.x:
            if self.pos.y < other.pos.y + other.size.y and self.pos.y + self.size.y > other.pos.y:
                return True