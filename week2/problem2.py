import sys


def main():

    paragraph2 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur rhoncus tincidunt sem nec gravida. Sed id convallis quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus dui purus, ornare vitae metus vitae, feugiat ultricies ipsum. Etiam id ante quis purus rhoncus egestas. Donec vel ligula lacinia, iaculis ipsum vitae, vulputate nunc. Aliquam tellus libero, sagittis quis massa elementum, semper sodales lacus. Sed justo arcu, lobortis quis bibendum ac, fermentum ut mi. Quisque faucibus ex vitae sapien aliquam blandit. Donec fringilla sit amet augue id venenatis. Integer at nibh quis justo consectetur posuere. Nulla facilisis mi massa, sed congue lectus vehicula sed. Quisque placerat ultrices est congue vestibulum. Maecenas fermentum purus et ipsum volutpat, eu convallis risus interdum. Donec vel nunc suscipit, venenatis mi at, convallis sapien. Integer ut metus id neque rhoncus commodo."""
    # the string paragrapph has 1003 characters
    # not correct; the extra tabs have extended the string; please retry
    print(len(paragraph2))

    # the substring 'it' occurs 13 times
    print(paragraph2.count("it"))

    # Converting the text into lowercase
    print(paragraph2.lower())

    # Replace all 'i' with '*'
    print(paragraph2.replace("i", "*"))
    
    return None


if __name__ == "__main__":
    sys.exit(main())
