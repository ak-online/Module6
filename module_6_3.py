class Horse:
    x_distance = 0
    _sound = 'Frrr'

    def run(self, dx):
        self.x_distance = self.x_distance + dx
        return self.x_distance


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance = self.y_distance + dy
        return self.y_distance


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        self.pos_ = (self.x_distance, self.y_distance)
        return self.pos_

    def voice(self):
        print(f'Sound - {self.sound}')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
