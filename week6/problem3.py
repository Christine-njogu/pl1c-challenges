import sys

"""
Notes:
- Excellent! I think you can do better. 
- This implementation uses two while loops so that for a long string
it would take double the length of the string. Can you do it using 
one loop?
"""


def reverse_string(characters):
    # todo: add a docstring; see class notes on how to do this
    new_list = list()
    # fixme:
    while characters:
        new_list.append(characters.pop())
    y = 0
    reverse_str = ""
    while y < len(new_list):
        reverse_str += new_list[y]
        y += 1
    return reverse_str


def main():
    my_word = input("Enter a word: ")
    my_list = list(my_word)
    string_reversed = reverse_string(my_list)
    print(f"Original string: {my_word}")
    print(f"Reversed string: {string_reversed}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
