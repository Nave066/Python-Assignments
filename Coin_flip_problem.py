import random


def coin_flip():
    head_count = 0
    tail_count = 0
    no_of_turns = int(input("Enter No of Turns the coin need to be tossed"))
    if no_of_turns > 0:
        for i in range(no_of_turns):
            random_flip = random.uniform(0, 1)
            if random_flip < 0.5:
                tail_count += 1
            else:
                head_count += 1
    else:
        print("Please Enter Only positive Values")
    print(tail_count)
    print(head_count)
    head_percent = (head_count / no_of_turns) * 100
    print("Head Percent is " + str(head_percent) + "%")
    tail_percent = (tail_count / no_of_turns) * 100
    print("Tail Percent is " + str(tail_percent) + "%")


coin_flip()
