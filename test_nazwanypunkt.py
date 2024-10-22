from nazwany_punkt import Nazwany_punkt
from punkt import Point


def main():
    a: Nazwany_punkt = Nazwany_punkt(3, 4, "latarnia")
    print(a)
    a.move(-2, 5)
    print(a)
    print(a.__dict__)
    print(type(a))
    b: Nazwany_punkt = Nazwany_punkt(7, 0, "morze")
    c: Point = Point(5, 9)

    print(issubclass(Point, Point))
    print(issubclass(Point, Nazwany_punkt))
    print(issubclass(Nazwany_punkt, Point))

    print(isinstance(a, Point))
    print(isinstance(a, Nazwany_punkt))
    print(isinstance(c, Nazwany_punkt))
    print(dir(a))

    del a
    print("Obiekt a został usunięty")


if __name__ == "__main__":
    main()