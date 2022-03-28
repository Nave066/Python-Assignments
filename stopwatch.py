import time


def time_convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


if __name__ == "__main__":
    input("Press Enter to start")
    start_time = time.time()

    input("Press Enter to stop")
    end_time = time.time()

    time_lapsed = end_time - start_time
    print(time_convert(time_lapsed))
