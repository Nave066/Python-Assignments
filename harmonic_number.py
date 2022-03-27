# Nth harmonic Number
def harmonic(uservalue):
    if uservalue < 0:
        return print("Invalid Input")
    harmonic_result = 0
    for iteration in range(1, uservalue + 1):
        harmonic_result += 1/iteration
    return harmonic_result


if __name__ == "__main__":
    userinput = int(input("Enter Number: "))
    print("The result is {:.3f}".format(harmonic(userinput)))
