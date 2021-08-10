import sys
import ui
import handle_files
import copy


def make_word_cards_group():
    word_cards = {}
    list_labels = ["Base language: ", "It's pair: "]
    for i in range(0, 2):
        card = ui.get_inputs(list_labels, "")
        word_cards[card[0]] = card[1]
    return word_cards


def transform_data_to_double_language_group(data, index):
    new_pairs = copy.deepcopy(data[index])
    for key in data[index]:
        new_pairs[new_pairs[key]] = key
    return new_pairs


def ask_back_words(data, index=0):
    both_language_cards = transform_data_to_double_language_group(data, index)
    for items in both_language_cards:
        answer = input(items + ": ")
        if answer == both_language_cards[items]:
            print("Correct!")
        else:
            print("Wrong")


def handle_menu():
    options = ["Add new word cards",
               "Ask back the words",
               "Check the saved word cards"]

    ui.print_menu("Main menu", options, "Exit program")


def handle_ask_back_menu():
    options = ["Ask back from the whole stack",
               "Ask back from a single group",
               "Ask back from multiple groups"]
    ui.print_menu("Ask back words", options, "Back")


def ask_back_option(cards):
    handle_ask_back_menu()
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        for i in range(0, len(cards)):
            ask_back_words(cards, i)
    elif option == "2":
        group_number = ui.get_inputs(["Please enter the number of the group: "], "")
        if group_number[0].isnumeric():
            if (int(group_number[0]) > 0 and int(group_number[0]) <= len(cards)):
                ask_back_words(cards, int(group_number[0])-1)
            else:
                ui.print_error_message("Wrong input range")
        else:
            ui.print_error_message("Wrong input type")
    elif option == "3":
        group_numbers = ui.get_inputs(["Please enter the numbers of the groups: "], "")
        indexes = group_numbers[0].split(" ")
        for item in indexes:
            if item.isnumeric():
                if (int(item) > 0 and int(item) <= len(cards)):
                    ask_back_words(cards, int(item)-1)
                else:
                    ui.print_error_message("Wrong input range")
            else:
                ui.print_error_message("Wrong input type")


def choose(FILE_NAME):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        cards = make_word_cards_group()
        handle_files.write_words_to_file(cards, "word_cards.csv")

    elif option == "2":
        cards = handle_files.read_words_from_file(FILE_NAME)
        ask_back_option(cards)
    elif option == "3":
        print(handle_files.read_words_from_file(FILE_NAME))
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")
