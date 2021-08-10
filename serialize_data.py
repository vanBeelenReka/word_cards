import copy


def serialize_card(card):
    return str(card[0] + "--" + card[1] + ";")


def serialize_cards(cards):
    cards_serialized = map(serialize_card, cards)
    return ''.join(cards_serialized)


def deserialize_lines_to_cards(raw_data):
    pairs = []
    for line in raw_data:
        word_cards_dic = {}
        word_pairs = line.split(";")
        for word_items in word_pairs[0:-1]:
            words = word_items.split("--")
            word_cards_dic[words[0]] = words[1]
        pairs.append(word_cards_dic)
    return pairs


def deserialize_data_to_double_language_group(data, index):
    dic = copy.deepcopy(data[index])
    for key in data[index]:
        dic[dic[key]] = key
    return dic
