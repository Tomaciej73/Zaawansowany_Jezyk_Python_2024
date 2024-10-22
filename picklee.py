import pickle
from nazwany_punkt import Nazwany_punkt
from punkt import Point
def main():

    point1 = Point(1, 2)
    point2 = Point(3, 4)
    named_point1 = Nazwany_punkt(5, 6, "A")
    named_point2 = Nazwany_punkt(7, 8, "B")
    points = [point1, point2, named_point1, named_point2]

    with open("punkty.pkl", "wb") as file:
        pickle.dump(points, file)

if __name__ == "__main__":
    main()