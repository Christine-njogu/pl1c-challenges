import sys


def main():
    user_sentence = input("Enter a sentence: ")
    user_list = user_sentence.split()
    for count, items in enumerate(user_list, 0):
        print(f"{count} -> {items}")
    return 0


if __name__ == "__main__":
    sys.exit(main())