import sys


def repeat_characters(word, factor):
    # todo: add a docstring; see class notes on how to do this
    new_word = ""
    for items in word:
        new_word += (items * factor)
    return new_word


def main():
    user_word = input("Enter a sequence of characters: ")
    repeated_seq = repeat_characters(user_word, 4)
    print(repeated_seq)

    return 0


if __name__ == "__main__":
    sys.exit(main())
