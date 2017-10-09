
import math

class Particle:
    def __init__(self, pos, v=(0,0), r=0.1, fixed=False, collides=True):
        self.r = r

        self.x = pos[0]
        self.y = pos[1]

        self.vx = v[0]
        self.vy = v[1]

        self.space = None

        self.fixed = fixed
        self.collides = collides


    def _distance(self, p):
        return math.sqrt((self.x - p.x)**2 +
                         (self.y - p.y)**2)


    def _collide(self):
        if not self.collides:
            return False

        # Collide with others
        others = self.space.particles - {self}
        for p in others:
            if p._distance(self) < self.r:
                return True

        return False


    def update(self, dt):

        # Collide
        if self._collide():
            return

        if self.fixed:
            return

        # Apply gravity
        self.vy += dt * self.space.g

        self.x = self.x + dt * self.vx
        self.y = self.y + dt * self.vy


