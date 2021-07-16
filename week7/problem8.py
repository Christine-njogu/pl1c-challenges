import random
import sys
import struct


def main():
    with open('binary_integers.bin', 'wb') as f:
        integers = random.choices(range(0, 200), k=1000)
        for items in integers:
            data = struct.pack('i', items)
            f.write(data)


if __name__ == "__main__":
    sys.exit(main())
