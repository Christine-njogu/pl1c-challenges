import sys

"""
Notes:
- Good function naming. Clear code. 
- Does your program consider case?
"""


def palindrome_check(word):
    # todo: add a docstring; see class notes on how to do this
    word_reverse = word[::-1]
    if word == word_reverse:
        print("The word is a palindrome")
    else:
        print("Word is not a palindrome")
    return None


def main():
    my_word = input("Enter a word: ")
    palindrome_check(my_word)

    return 0


if __name__ == "__main__":
    sys.exit(main())
