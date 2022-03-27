import math


def wind_chill(temp, wind_speed):
    return 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * math.pow(wind_speed, 0.16)


if __name__ == "__main__":
    temperature = int(input("Enter Temperature: "))
    speed = int(input("Enter Wind speed: "))
    print("Wind Chill is ", round(wind_chill(temperature, speed)))
