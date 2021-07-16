import sys
import pathlib


def main():
    my_path = pathlib.Path("cortex/morsel/sunshine/nothing.txt")
    with my_path.open('r') as f:
        data = f.read()
        print(data)
    image_path = pathlib.Path("cortex/printer/at/profession/image.jpg")
    with image_path.open('rb') as f:
        my_image = f.read()
        print(my_image)
    orange_path = pathlib.Path("cortex/printer/notorious/orange.json")
    print(f"Complete path of orange file: {orange_path.absolute()}")
    print(f"Current directory: {my_path.cwd()}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
