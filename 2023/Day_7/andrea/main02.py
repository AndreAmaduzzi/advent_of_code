"""
7th December, 2023
"""


type_to_value = {
    "High": 1,
    "OnePair": 2,
    "TwoPair": 3,
    "Three": 4,
    "Full": 5,
    "Four": 6,
    "Five": 7,
}

card_to_value = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 0,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def type_hand(hand):
    ch_aux = set()
    for ch in hand:
        if ch != "J":
            ch_aux.add(ch)

    j_count = str(hand).count("J")
    count = [0, 0, 0, 0, 0]
    char = ["", "", "", "", ""]

    if j_count == 5:
        return "Five"

    for idx, x in enumerate(ch_aux):
        for check in hand:
            if x == check and check != "J":
                count[idx] += 1
                char[idx] = x

    if j_count > 0:
        max_id = 0
        max = 0
        for i in range(len(count)):
            if (count[i] > max) or (
                count[i] == max and card_to_value[char[i]] > card_to_value[char[max_id]]
            ):
                max = count[i]
                max_id = i
        count[max_id] += j_count

    if len(ch_aux) == 5:
        return "High"
    elif len(ch_aux) == 4:
        return "OnePair"
    elif len(ch_aux) == 3:
        if count[0] == 3 or count[1] == 3 or count[2] == 3:
            return "Three"
        else:
            return "TwoPair"
    elif len(ch_aux) == 2:
        if count[0] == 4 or count[1] == 4:
            return "Four"
        else:
            return "Full"
    else:
        return "Five"


def check_minus_hand(hand1, hand2, type):
    res = False
    for x in range(5):
        if card_to_value[hand1[x]] == card_to_value[hand2[x]]:
            continue
        elif card_to_value[hand1[x]] > card_to_value[hand2[x]]:
            res = True
            break
        else:
            res = False
            break

    return res


def order_hand(list_hand):
    list_ordered = []
    for x in list_hand:
        if len(list_ordered) == 0:
            list_ordered.append(x)
            continue
        for it in range(len(list_ordered)):
            if list_ordered[it][2] > x[2]:
                list_ordered.insert(it, x)
                break
            elif list_ordered[it][2] == x[2]:
                if check_minus_hand(x[0], list_ordered[it][0], x[2]) == True:
                    if it == len(list_ordered) - 1:
                        list_ordered.append(x)
                else:
                    list_ordered.insert(it, x)
                    break
            elif it == len(list_ordered) - 1:
                list_ordered.append(x)
    return list_ordered


def main():
    with open("input_andy.txt", "r") as f:
        lines = f.readlines()

    file1 = open("output_mycheck.txt", "w")

    list_hand = []

    for line in lines:
        words = line.split(" ")
        hand = words[0]
        value = int(words[1])
        type = []
        aux_list = [hand, value, type]
        list_hand.append(aux_list)

    for it in list_hand:
        type = type_hand(it[0])
        it[2] = type_to_value[type]

    list_ordered = order_hand(list_hand)

    sum = 0

    for idx, item in enumerate(list_ordered):
        sum += (idx + 1) * item[1]

    for line in list_ordered:
        file1.write(line[0] + " " + str(line[1]) + " " + str(line[2]) + "\n")

    print("Soluzione:")
    print(sum)

    file1.close()


if __name__ == "__main__":
    main()
