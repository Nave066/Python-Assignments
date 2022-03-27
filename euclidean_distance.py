import math


def euclidean(p1, p2):
    return math.sqrt(((int(p1[0]) - int(p2[0])) ** 2) + ((int(p1[1]) - int(p2[1])) ** 2))


if __name__ == "__main__":
    a1, b1, a2, b2 = input("Enter the Values of a1,b1,a2,b2: ").split(",", 4)
    point1 = [a1, b1]
    point2 = [a2, b2]
    print("{:.3f}".format(euclidean(point1, point2)))
