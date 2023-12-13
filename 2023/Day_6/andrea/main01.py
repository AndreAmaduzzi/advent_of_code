"""
6th December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    time = []
    distance = []
    
    for word in lines[0].split():
        if word.isdecimal():
            time.append(int(word))

    for word in lines[1].split():
        if word.isdecimal():
            distance.append(int(word))

    print(time)
    print(distance)
    num_test = len(time)
    count_success = []

    for attend in range(num_test):
        count = 0
        # print('Attend = ' + str(attend))
        for i in range(time[attend]):
            vel = i + 1
            time_move = time[attend] - (i + 1)
            distance_move = vel * time_move
            # print(i + 1)
            # print('time_move = ' + str(time_move))
            # print('distance_move = ' + str(distance_move))
            if distance_move > distance[attend]:
                count += 1
        count_success.append(count)
        # print()
    
    print(count_success)
    
    prod = 1
    for x in count_success:
        prod *= x

    print('Soluzione:')
    print(prod)


if __name__ == "__main__":
    main()