#!/usr/bin/env python3

import time

import space
import particle


FPS = 30

FLOOR = particle.Particle((0,0), fixed=True)

def simulate_debug(space):
    space.reset()
    t0 = time.time()
    while True:
        t = time.time() - t0

        if t > 5:
            FLOOR.fixed = False

        space.update()
        space.print_state()
        time.sleep(1.0/FPS)



if __name__ == "__main__":
    s = space.Space(9.81)

    s.add_particle(FLOOR)
    s.add_particle(particle.Particle((0, 16)))
    s.add_particle(particle.Particle((0, 17.2)))
    s.add_particle(particle.Particle((0, 18.4)))
    s.add_particle(particle.Particle((0, 19.6)))
    s.add_particle(particle.Particle((0, 20.8)))

    simulate_debug(s)

