"""
7th December, 2023
"""

card_val = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def read_data(path):
    with open(path, "r") as f:
        lines = f.readlines()

    list_data = []
    for line in lines:
        split_line = line.split(" ")
        my_data = {"cards": [], "bid": [], "temp_rank": [], "rank": [], "vals": []}

        my_data["cards"] = split_line[0]
        my_data["bid"] = int(split_line[1].replace("\n", ""))
        my_data["temp_rank"] = 0
        my_data["rank"] = 0
        my_data["vals"] = [card_val[card] for card in my_data["cards"]]
        list_data.append(my_data)

    return list_data


def main():
    input_path = "input.txt"
    data = read_data(input_path)
    # print("data:", data)

    for sample in data:
        hand = sample["cards"]

        set_hand = set(hand)
        dict_hand = {}
        for el in set_hand:
            dict_hand[el] = 0
        for card in hand:
            dict_hand[card] += 1

        counts = list(dict_hand.values())
        sorted_counts = sorted(counts, reverse=True)
        if sorted_counts[0] == 5:
            sample["temp_rank"] = 7
        elif sorted_counts[0] == 4:
            sample["temp_rank"] = 6
        elif sorted_counts[0] == 3:
            if sorted_counts[1] == 2:
                sample["temp_rank"] = 5
            else:
                sample["temp_rank"] = 4
        elif sorted_counts[0] == 2:
            if sorted_counts[1] == 2:
                sample["temp_rank"] = 3
            else:
                sample["temp_rank"] = 2
        else:
            sample["temp_rank"] = 1

    sorted_data = sorted(data, key=lambda d: d["temp_rank"])

    rank_samples = {"1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}

    sorted_rank_samples = rank_samples

    for sample in sorted_data:
        rank_samples[str(sample["temp_rank"])].append(sample)

    for rank, rank_sample in rank_samples.items():
        # inside list of all hands with the same temp_rank
        # sort all hands according to value of first card, then second, then third...
        sorted_rank_samples[rank] = sorted(rank_sample, key=lambda x: x["vals"])

    i = 0
    wins = 0
    for rank, sorted_rank_list in sorted_rank_samples.items():
        for sample in sorted_rank_list:
            i += 1
            wins += sample["bid"] * i

    print("\nwins:", wins)


if __name__ == "__main__":
    main()
