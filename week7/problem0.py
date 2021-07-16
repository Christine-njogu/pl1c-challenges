import sys
import io


def main():
    with io.open('exotic.txt', encoding='koi8-r') as f:
        text = f.read()
        encoded_text = text.encode('utf-8')
        my_text = encoded_text.decode('utf-8')
    with io.open('exotic.txt', 'w', encoding='utf-8') as f:
        f.write(my_text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
