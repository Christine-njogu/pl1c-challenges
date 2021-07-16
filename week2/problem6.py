import os
import sys


def main():
    txt_a = "apache license"
    txt_b = "version 2.0, january 2004"
    txt_c = "http://www.apache.org/licenses/"

    x = txt_a.center(50, " ")
    y = txt_b.center(50, " ")
    z = txt_c.center(50, " ")
    print(x.title())
    print(y.title())
    print(z)

    return None


if __name__ == "__main__":
    sys.exit(main())
