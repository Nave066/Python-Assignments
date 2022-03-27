def leapyear():
    print("To find whether the given year is leap year or not")
    input_year = int(input("Enter the year: "))
    if len(str(input_year)) == 4:
        if (input_year % 400 == 0) and (input_year % 100 == 0):
            print("{0} is a leap year".format(input_year))
        elif (input_year % 4 == 0) and (input_year % 100 != 0):
            print("{0} is a leap year".format(input_year))
        else:
            print("{0} is not a leap year".format(input_year))
    else:
        print("Enter the Valid year")


if __name__ == "__main__":
    leapyear()
