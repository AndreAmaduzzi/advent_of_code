"""
6st December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    str_time = ''
    str_distance = ''
    
    for word in lines[0].split():
        if word.isdecimal():
            str_time += word

    for word in lines[1].split():
        if word.isdecimal():
            str_distance += word

    print(str_time)
    print(str_distance)
    
    time = int(str_time)
    distance = int(str_distance)
    
    count_success = 0

    for i in range(time):
        vel = i + 1
        time_move = time - (i + 1)
        distance_move = vel * time_move
        if distance_move > distance:
            count_success += 1
    # print()
    
    print('Soluzione:')
    print(count_success)


if __name__ == "__main__":
    main()