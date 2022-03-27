def find_triplets(inp, length):
    present = False
    for i in range(0, length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if inp[i] + inp[j] + inp[k] == 0:
                    print("The triplets found With values: {},{},{}".format(inp[i], inp[j], inp[k]))
                    present = True
    if not present:
        return print("No Triplet found")


if __name__ == "__main__":
    array_input = [3, 6, -9, 5, -7, -6, 1, -9]
    find_triplets(array_input, len(array_input))
