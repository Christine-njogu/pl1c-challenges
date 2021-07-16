import sys
import pathlib


def main():
    first_folder = pathlib.Path("./mars")
    if not first_folder.exists():
        first_folder.mkdir()
    else:
        print(f"Warning: File already exists")
    second_folder = first_folder / "mist"
    if not second_folder.exists():
        second_folder.mkdir()
    else:
        print(f"Warning: File already exists")
    print(second_folder.absolute())
    nut_path = second_folder / "reduced-nut.txt"
    with nut_path.open('w') as f:
        f.write("Nuts are of different sizes. Their measurement could be given in imperial or metric units.")
        f.write("\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
