from math import sqrt


def quadratic(d, e, f):
    quad = (e ** 2) - 4 * d * f
    if quad > 0:
        root1 = (((-e) + sqrt(quad)) / (2 * d))
        root2 = (((-e) - sqrt(quad)) / (2 * d))
        return print("The two roots are : {:.3f} and {:.3f} ".format(root1, root2))
    elif quad == 0:
        return print("The root is: {:.3f}".format((-e) / 2 * d))
    else:
        return print("No Roots")


if __name__ == "__main__":
    a, b, c = input("The value of a,b,c: ").split(",", 3)
    a = float(a)
    b = float(b)
    c = float(c)
    quadratic(a, b, c)
