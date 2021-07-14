import sys
import ui


def make_word_cards_group():
    word_cards = {}
    list_labels = ["Base language: ", "It's pair: "]
    for i in range(0, 2):
        card = ui.get_inputs(list_labels, "")
        word_cards[card[0]] = card[1]
    return word_cards


def ask_back_words(cards):
    for items in cards:
        print(items,  cards[items])
        answer = input(items + " ")
        if answer == cards[items]:
            print("Correct!")
        else:
            print("Wrong")


def make_cards_clean_to_write_in_a_file(cards):
    clean_cards = list(cards.items())
    return clean_cards


def write_words_to_file(cards, file_name):
    clean_cards = make_cards_clean_to_write_in_a_file(cards)
    with open(file_name, "w") as file:
        file.write(serialize_cards(clean_cards))


def serialize_card(card):
    return str(card[0] + "-" + card[1] + ";")


def serialize_cards(cards):
    cards_serialized = map(serialize_card, cards)
    return ''.join(cards_serialized)


def deserialize_lines_to_cards(lines):
    word_cards_dic = {}
    for item in lines:
        word_groups = item.split(";")
        for groups_items in word_groups[0:-1]:
            word_pairs = groups_items.split("-")
            word_cards_dic[word_pairs[0]] = word_pairs[1]
    return word_cards_dic


def read_words_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    return deserialize_lines_to_cards(lines)


def handle_menu():
    options = ["Add new word cards",
               "Ask back the words",
               "Check the saved word cards"]

    ui.print_menu("Main menu", options, "Exit program")


def choose(FILE_NAME):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        cards = make_word_cards_group()
        write_words_to_file(cards, "word_cards.csv")

    elif option == "2":
        cards = read_words_from_file(FILE_NAME)
        ask_back_words(cards)
    elif option == "3":
        print(read_words_from_file(FILE_NAME))
    elif option == "0":
            sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def main():
    FILE_NAME = "word_cards.csv"
    while True:
        handle_menu()
        try:
            choose(FILE_NAME)
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == "__main__":
    main()
