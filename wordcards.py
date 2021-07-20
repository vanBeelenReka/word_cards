import sys
import ui
import handle_files


def make_word_cards_group():
    word_cards = {}
    list_labels = ["Base language: ", "It's pair: "]
    for i in range(0, 2):
        card = ui.get_inputs(list_labels, "")
        word_cards[card[0]] = card[1]
    return word_cards


def ask_back_words(cards):
    for items in cards:
        answer = input(items + ": ")
        if answer == cards[items]:
            print("Correct!")
        else:
            print("Wrong")


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
        handle_files.write_words_to_file(cards, "word_cards.csv")

    elif option == "2":
        cards = handle_files.read_words_from_file(FILE_NAME)
        ask_back_words(cards)
    elif option == "3":
        print(handle_files.read_words_from_file(FILE_NAME))
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
