def powerofn_problem(user):
    if 0 <= user < 31:
        return pow(2, user)
    else:
        return print("Invalid input")


if __name__ == "__main__":
    userinput = int(input("Enter the value between 0 and 31: "))
    print("The power of {0} is {1}".format(userinput, powerofn_problem(userinput)))

