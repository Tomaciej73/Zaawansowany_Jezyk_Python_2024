'''Zadanie 1 Klasy 1.1'''
class Point:
    __slots__ = ('_x', '_y')

    def __init__(self, x: float, y: float) -> None:
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = float(value)

    @x.deleter
    def x(self):
        del self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = float(value)

    @y.deleter
    def y(self):
        del self._y

    def __repr__(self):
        return f'Point({self._x}, {self._y})'

    def __str__(self):
        return f'Point({self._x}, {self._y})'

    def move(self, delta_x: float, delta_y: float):
        self._x += delta_x
        self._y += delta_y