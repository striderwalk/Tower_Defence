import math

class Bullet:
    def __init__(self, pos,angle, speed):
        self.pos = pos
        self.angle = angle ## radients
        self.speed = speed


    def move(self):
        new_x = self.pos[0] + self.speed*math.sin(self.angle)
        new_y = self.pos[1] + self.speed*math.cos(self.angle)

        self.pos = (new_x, new_y)

        return self.pos

    def update(self, enemys):
        hits = []
        for enemy in enemys:
            if enemy.body.collidepoint(self.pos):
                print(enemy)
                hits.append(enemy)

        if hits is []:
            return 
        min_dis = 1_000_0000_000_000
        min_index =  -1

        for index, i in enumerate(hits):
            dis =  abs(i.pos[0] - self.pos[0]) + abs(i.pos[1] - self.pos[1])
            if dis < min_dis:
                min_dis = dis
                min_index = index


        if min_index != -1:
            hits[min_index].die()

            return "die"
 