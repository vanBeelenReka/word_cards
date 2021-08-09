import serialize_data


def make_cards_clean_to_write_in_a_file(cards):
    clean_cards = list(cards.items())
    return clean_cards


def write_words_to_file(cards, file_name):
    clean_cards = make_cards_clean_to_write_in_a_file(cards)
    with open(file_name, "a") as file:
        file.write(serialize_data.serialize_cards(clean_cards))
        file.write('\n')


def read_words_from_file(file_name):
    with open(file_name, "r") as file:
        raw_data = file.readlines()
    return serialize_data.deserialize_lines_to_cards(raw_data)
