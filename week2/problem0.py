import sys


def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"The user  {name} of age {age} is learning Python programming")
    return None


if __name__ == "__main__":
    sys.exit(main())
