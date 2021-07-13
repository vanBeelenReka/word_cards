

def make_word_cards_group():
    word_cards = {}
    for i in range(0, 2):
        k, v = make_word_pair()
        word_cards[k] = v

    return word_cards


def make_word_pair():
    first_word = input("Please, enter the base language word: ")
    second_word = input("Please, enter the pair of the privious word: ")

    return first_word, second_word


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

        for item in clean_cards:
            file.write(str(item[0] + "-" + item[1] + ";"))


def transform_exported_data(lines):
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
    word_cards_dic = transform_exported_data(lines)
    print(word_cards_dic)


def main():
    cards = make_word_cards_group()
    # cards = {'alma': 'appel', 'korte': 'pear'}
    print(cards)
    ask_back_words(cards)
    write_words_to_file(cards, "word_cards.csv")
    read_words_from_file("word_cards.csv")


if __name__ == "__main__":
    main()