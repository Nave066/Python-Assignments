import random


def gambling_game(goal, stack):
    count = 0
    win = 0
    lose = 0
    while stack != goal:
        if stack != 0:
            count += 1
            random_value = random.randint(0, 1)
            if random_value == 1:
                stack += 1
                win += 1
            else:
                stack -= 1
                lose += 1
        else:
            break
    print("The No of times I bet: " + str(count))
    if win > lose:
        print("I won the game, Reached my goal")
    else:
        print("I lost the game, No money left")
    print("Winning percentage: {:.3f}".format((win * 100) / count))
    print("Losing percentage: {:.3f}".format((lose * 100) / count))


if __name__ == "__main__":
    goal_value = int(input("My goal is to make:  "))
    stack_amount = int(input("I'm going to invest: "))
    # no_of_turns = int(input("No of turns I need to play: "))
    gambling_game(goal_value, stack_amount)
