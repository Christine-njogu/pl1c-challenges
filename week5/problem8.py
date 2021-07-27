import sys
import string


def main():
    text = """When Princess Mary came down, Prince Vasíli and his son were already in the drawing room, talking to 
    the little princess and Mademoiselle Bourienne. When she entered with her heavy step, treading on her heels, 
    the gentlemen and Mademoiselle Bourienne rose and the little princess, indicating her to the gentlemen, 
    said: “Voilà Marie!” Princess Mary saw them all and saw them in detail. She saw Prince Vasíli’s face, serious for 
    an instant at the sight of her, but immediately smiling again, and the little princess curiously noting the 
    impression “Marie” produced on the visitors. And she saw Mademoiselle Bourienne, with her ribbon and pretty face, 
    and her unusually animated look which was fixed on him, but him she could not see, she only saw something large, 
    brilliant, and handsome moving toward her as she entered the room. Prince Vasíli approached first, and she kissed 
    the bold forehead that bent over her hand and answered his question by saying that, on the contrary, 
    she remembered him quite well. Then Anatole came up to her. She still could not see him. She only felt a soft 
    hand taking hers firmly, and she touched with her lips a white forehead, over which was beautiful light-brown 
    hair smelling of pomade. When she looked up at him she was struck by his beauty. Anatole stood with his right 
    thumb under a button of his uniform, his chest expanded and his back drawn in, slightly swinging one foot, and, 
    with his head a little bent, looked with beaming face at the princess without speaking and evidently not thinking 
    about her at all. Anatole was not quick-witted, nor ready or eloquent in conversation, but he had the faculty, 
    so invaluable in society, of composure and imperturbable self-possession. If a man lacking in self-confidence 
    remains dumb on a first introduction and betrays a consciousness of the impropriety of such silence and an 
    anxiety to find something to say, the effect is bad. But Anatole was dumb, swung his foot, and smilingly examined 
    the princess’ hair. It was evident that he could be silent in this way for a very long time. “If anyone finds 
    this silence inconvenient, let him talk, but I don’t want to,” he seemed to say. Besides this, in his behavior to 
    women Anatole had a manner which particularly inspires in them curiosity, awe, and even love—a supercilious 
    consciousness of his own superiority. It was as if he said to them: “I know you, I know you, but why should I 
    bother about you? You’d be only too glad, of course.” Perhaps he did not really think this when he met women—even 
    probably he did not, for in general he thought very little—but his looks and manner gave that impression. The 
    princess felt this, and as if wishing to show him that she did not even dare expect to interest him, she turned 
    to his father. The conversation was general and animated, thanks to Princess Lise’s voice and little downy lip 
    that lifted over her white teeth. She met Prince Vasíli with that playful manner often employed by lively chatty 
    people, and consisting in the assumption that between the person they so address and themselves there are some 
    semi-private, long-established jokes and amusing reminiscences, though no such reminiscences really exist—just as 
    none existed in this case. Prince Vasíli readily adopted her tone and the little princess also drew Anatole, 
    whom she hardly knew, into these amusing recollections of things that had never occurred. Mademoiselle Bourienne 
    also shared them and even Princess Mary felt herself pleasantly made to share in these merry reminiscences. """
    marks = string.punctuation
    for items in text:
        if items in marks:
            text = text.replace(items, "")
    paragraph_list = text.lower().split()
    three_letter_words = []
    four_letter_words = []
    five_letter_words = []
    other_list = []
    three_letter_dict = {}
    four_letter_dict = {}
    five_letter_dict = {}
    for words in paragraph_list:
        if len(words) == 3:
            three_letter_words.append(words)
        elif len(words) == 4:
            four_letter_words.append(words)
        elif len(words) == 5:
            five_letter_words.append(words)
        else:
            other_list.append(words)
    for words in three_letter_words:
        three_letter_dict[words] = three_letter_words.count(words)
    for words in four_letter_words:
        four_letter_dict[words] = four_letter_words.count(words)
    for words in five_letter_words:
        five_letter_dict[words] = five_letter_words.count(words)
    alphabetic_three_letter = {key: three_letter_dict[key] for key in sorted(three_letter_dict)}
    print("\n3-letter words:")
    print("-" * 70)
    for words, count in alphabetic_three_letter.items():
        print(f"{words}: {count}")
    alphabetic_four_letter = {key: four_letter_dict[key] for key in sorted(four_letter_dict)}
    print("\n4-letter words:")
    print("-" * 70)
    for words, count in alphabetic_four_letter.items():
        print(f"{words}: {count}")
    alphabetic_five_letter = {key: five_letter_dict[key] for key in sorted(five_letter_dict)}
    print("\n5-letter words:")
    print("-" * 70)
    for words, count in alphabetic_five_letter.items():
        print(f"{words}: {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())