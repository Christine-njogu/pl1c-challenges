import sys


def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    year_of_birth = input("Enter the year of birth: ")
    y = int(year_of_birth) + 77
    print(f"The person {name} is {age} years now. She will be 77 years in {y}.")


if __name__ == "__main__":
    sys.exit(main())
