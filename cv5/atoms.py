import playground
import random
import sys

class Atom(object):
    def __init__(self, pos_x, pos_y, rad, color, speed_x, speed_y):
        self.pos_x = float(pos_x)
        self.pos_y = float(pos_y)
        self.rad = float(rad)
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self, width, height):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        if self.pos_x + self.rad >= width or self.pos_x - self.rad <= 0:
            self.speed_x *= -1
        elif self.pos_y + self.rad >= height or self.pos_y - self.rad <= 0:
            self.speed_y *= -1

    def to_tuple(self):
        return (self.pos_x, self.pos_y, self.rad, self.color)
        

class ExampleWorld(object):

    def __init__(self, count, width, height):
        self.size_x = width
        self.size_y = height
        self.atoms = []

        for i in range(count):
            self.atoms.append(self.random_atom())

        # nasledujici atomy po generovani nahodnych atomu muzete smazat
        #self.atoms.append(Atom(60, 60, 30, 'red'))
        #self.atoms.append(Atom(120, 160, 20, 'green'))

    def random_atom(self):
        rad = random.randint(10, 50)
        pos_x = random.randint(rad, self.size_x - rad)
        pos_y = random.randint(rad, self.size_y - rad)
        speed_x = random.randint(1,15)
        speed_y = random.randint(1, 15)

        color = random.choice(list(playground.Colors)).value

        return Atom(pos_x,pos_y,rad,color,speed_x,speed_y)




    def tick(self, size_x, size_y):
        tupled_atoms = []
        for atom in self.atoms:
            atom.move(size_x,size_y)
            tupled_atoms.append(atom.to_tuple())
        return tuple(tupled_atoms)


class FallDownAtom(Atom):
    g = 3.0
    damping = 0.8

    def __init__(self, pos_x, pos_y, rad, color, speed_x, speed_y):
        super().__init__(pos_x, pos_y, rad, color, speed_x, speed_y)

    def move(self, width, height):
       self.speed_y += self.g
       if self.speed_y < 0:
           self.speed_y *= self.damping
           self.speed_x *= self.damping
       super().move(width, height)





if __name__ == '__main__':
    size_x, size_y = 400, 300
    world = ExampleWorld(10, size_x, size_y)
    playground.run((size_x, size_y), world)
