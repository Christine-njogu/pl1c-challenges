import sys


def main():
    # String variable
    w = "पायथन एक अद्भुत प्रोग्रामिंग भाषा है जिसके माध्यम से मैं बहुत कुछ हासिल कर सकता हूं।"
    print(type(w))
    encoded = w.encode("utf-8")
    print(encoded)
    # Type bytes
    print((type(encoded)))

    return None


if __name__ == "__main__":
    sys.exit(main())
