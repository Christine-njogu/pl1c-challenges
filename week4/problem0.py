import sys

"""
Notes:
- I like the way you organise your code; I suspect this is not your first intro
to programming
- Your code is clear and you have good variable names.
"""
def main():
    list_with_values = list(input("Enter a 10 character word: "))
    length_of_word = len(list_with_values)
    word_dict = {}
    if length_of_word == 10:
        for items in list_with_values:
            word_dict[items] = list_with_values.count(items)
        print(word_dict)
    else:
        if length_of_word < 10:
            print("The word is too short.")
        else:
            print("The word is too long.")
    return 0 # if on Windows os.EX_OK fails


if __name__ == "__main__":
    sys.exit(main())
