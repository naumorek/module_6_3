'''Задача "Мифическое наследование":
Необходимо написать 3 класса:
Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
x_distance = 0 - пройденный путь.
sound = 'Frrr' - звук, который издаёт лошадь.
И методами:
run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
y_distance = 0 - высота полёта
sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
И методами:
fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
Также обладает методами:
move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
voice - который печатает значение унаследованного атрибута sound.
Пункты задачи:
Создайте классы родители: Horse и Eagle с методами из описания.
Создайте класс наследник Pegasus с методами из описания.
Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.

Пример результата выполнения программы:
Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

Вывод на консоль:
(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat

Примечания:
Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном наследовании: при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
Заметьте, что Pegasus издаёт звук "I train, eat, sleep, and repeat", т.к. по порядку сначала идёт наследование от Horse, а после от Eagle.
'''
class Horse:
    def __init__(self,x_distance = 0,y_distance=0,sound = 'Frrr'):
        self.x_distance=x_distance
        self.sound=sound
        super().__init__(y_distance)


    def run(self, dx):
        self.x_distance=self.x_distance+dx

class Eagle:
    def __init__(self,x_distance = 0, y_distance = 0,sound ='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound



    def fly(self, dy):
        self.y_distance = self.y_distance + dy

class Pegasus(Horse,Eagle):
    def __init__(self,x_distance=0,y_distance=0,sound=''):
        super().__init__(x_distance,y_distance)


    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):

        return [self.x_distance,self.y_distance]

    def voice(self):

        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
