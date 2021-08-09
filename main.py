import wordcards
import ui


def main():
    FILE_NAME = "word_cards.csv"
    while True:
        wordcards.handle_menu()
        try:
            wordcards.choose(FILE_NAME)
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == "__main__":
    main()
