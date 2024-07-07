class Horse:
    def __init__(self, x_distance, sound):
        self.sound = sound
        self.x_distance = x_distance
        print(self.sound, self.x_distance)

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance, sound):
        self.sound = sound
        self.y_distance = y_distance
        print(self.sound, self.y_distance)

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance, y_distance, sound):
        Horse.__init__(self, x_distance, sound)
        Eagle.__init__(self, y_distance, sound)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


# Проверка метода mro
print(Pegasus.mro())

# Создание объектов классов
l = Horse(0, 'Frrr')
l.run(22)
print(l.sound, l.x_distance)

e = Eagle(0, 'I train, eat, sleep, and repeat')
e.fly(33)
print(e.y_distance, e.sound)

p1 = Pegasus(0, 0, 'I train, eat, sleep, and repeat')
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()

