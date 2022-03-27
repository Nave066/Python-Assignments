def primeFactors(val):
    c = 2
    while val > 1:
        if val % c == 0:
            print(c)
            val = val / c
        else:
            c = c + 1


if __name__ == "__main__":
    inp = int(input("Enter the number: "))
    primeFactors(inp)
