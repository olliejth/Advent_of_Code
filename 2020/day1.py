
def count_occurences(letter: str, password: str) -> int:
    """Returns the number of occurences of a letter in a password"""
    counter = 0

    for l in password:
        if l == letter:
            counter += 1

    return counter


def reformat_input(input: str) -> dict:
    """Extracts the key information from a provided data string."""
    pword = input.split(" ")[-1]
    values = input.split(" ")[0]
    minimum = int(values.split("-")[0])
    maximum = int(values.split("-")[1])
    letter = input.split(" ")[1][0]

    return {
        "min": minimum,
        "max": maximum,
        "letter": letter,
        "password": pword
    }


def get_number_of_valid_passwords(data: list[str]) -> int:
    """Returns number of valid passwords in a provided list."""
    counter = 0
    for item in data:
        info_dict = reformat_input(item)
        occurences = count_occurences(
            info_dict["letter"], info_dict["password"])
        if occurences >= info_dict["min"] and occurences <= info_dict["max"]:
            counter += 1

    return counter


if __name__ == "__main__":
    # CODE
    with open("test_data.txt", "r", encoding="utf-8") as f_obj:
        password_data = [word.strip() for word in f_obj.readlines()]

    print(get_number_of_valid_passwords(password_data))
