

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


def main():
    # cards = make_word_cards_group()
    cards = {'alma': 'appel', 'korte': 'pear'}
    print(cards)
    ask_back_words(cards)


if __name__ == "__main__":
    main()