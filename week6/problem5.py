import sys

"""
Notes:
- Good but incomplete.
"""


def duplicate_characters(word):
    # todo: add a docstring; see class notes on how to do this
    new_word = ""
    for items in word:
        new_word += (items * 2)
    return new_word


def main():
    user_word = input("Enter a sequence of characters: ")
    duplicated_seq = duplicate_characters(user_word)
    print(duplicated_seq)

    return 0


if __name__ == "__main__":
    sys.exit(main())
