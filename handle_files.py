# TODO: refactor the deserialize function

def make_cards_clean_to_write_in_a_file(cards):
    clean_cards = list(cards.items())
    return clean_cards


def write_words_to_file(cards, file_name):
    clean_cards = make_cards_clean_to_write_in_a_file(cards)
    with open(file_name, "a") as file:
        file.write(serialize_cards(clean_cards))
        file.write('\n')


def read_words_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    return deserialize_lines_to_cards(lines)


def serialize_card(card):
    return str(card[0] + "--" + card[1] + ";")


def serialize_cards(cards):
    cards_serialized = map(serialize_card, cards)
    return ''.join(cards_serialized)


def deserialize_lines_to_cards(lines):
    pairs = []
    for item in lines:
        card_groups = item.split("\n")
        word_cards_dic = {}

        for card_group in card_groups[0:-1]:
            word_groups = card_group.split(";")

            for groups_items in word_groups[0:-1]:
                word_pairs = groups_items.split("--")
                word_cards_dic[word_pairs[0]] = word_pairs[1]
        pairs.append(word_cards_dic)
    return pairs


def split_multiple_data(data, symbol):
    splited_data = []
    for item in data[0:-1]:
        splited_data.append(item.split(symbol))
    return splited_data
