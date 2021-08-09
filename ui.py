def print_menu(title, list_options, exit_message):

    print()
    print(f"{title}:")
    for i in range(len(list_options)):
        print("{0:>8}{1}) {2}".format("(", i+1, list_options[i]))
    print("{0:>8}0) {1}".format("(", exit_message))


def print_error_message(message):
    print(f"Error: {message}")


def get_inputs(list_labels, title):
    print(title)
    user_data = []
    for lable in list_labels:
        user_data.append(input(lable + " "))
    return user_data
