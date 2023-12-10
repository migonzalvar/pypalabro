import random


def main():
    word_of_the_day = choose_word()
    print(word_of_the_day)
    print(f"La palabra tiene {len(word_of_the_day)} letras.")
    for attempt in range(5, 0, -1):
        print(f"Tienes {attempt} intentos.")
        guess = input("Escribe una palabra: ").strip().upper()

        if not guess:
            print("Gracias por jugar.")
            return

        if len(guess) != len(word_of_the_day):
            print(f"La palabra debe tener {len(word_of_the_day)} de letras.")
            continue

        if guess == word_of_the_day:
            print("¡Acertaste!")
            break

        result = check_word(word_of_the_day, guess)

        print()
        print(guess)
        print(result)
        print()
    else:
        print("¡No acertaste!")

    print(f"La palabra era {word_of_the_day}.")


def choose_word():
    with open("es.txt", "r", encoding="utf-8") as f:
        words = f.read().splitlines()
    return random.choice(words).upper()


def check_word(word, guess):
    """
    >>> check_word('AB', 'AB')
    '**'
    >>> check_word('AB', 'BA')
    '??'
    >>> check_word('AB', 'BZ')
    '?-'
    >>> check_word('AB', 'ZA')
    '-?'
    >>> check_word('AB', 'AZ')
    '*-'
    >>> check_word('AB', 'ZB')
    '-*'
    >>> check_word('AB', 'ZZ')
    '--'
    """

    result = []
    leftovers = list(word)

    # Primera pasada: letras correctas
    for idx, letter in enumerate(guess):
        if letter == word[idx]:
            leftovers.remove(letter)
            result.append("*")
        else:
            result.append("-")

    # Segunda pasada: letras en la palabra pero en otra posición
    for idx, letter in enumerate(guess):
        if letter == word[idx]:
            continue

        if letter in leftovers:
            leftovers.remove(letter)
            result[idx] = "?"

    return "".join(result)


if __name__ == "__main__":
    main()
