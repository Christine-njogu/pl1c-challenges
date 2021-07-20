import random
import sys


def main():
    character = 'A' + 'C' + 'G' + 'T'
    sequence = ''.join(random.choices(character, k=100))
    print(f"\nOriginal  DNA  sequence: {sequence}\tLength: {len(sequence)}")
    sequence2 = sequence.replace('A', 'U').replace('G', 'B').replace('C', 'G').replace('T', 'A').replace('B', 'C')
    print(f"Transcribed RNA sequence: {sequence2}\tLength: {len(sequence2)}")
    length_of_sequence = len(sequence2)
    step = 3
    codon_list = [sequence2[x: x+step] for x in range(0, length_of_sequence-1, step)]
    print(f"Number of codons in RNA: {len(codon_list)}")
    translated_codons = []
    for items in codon_list:
        if items == 'UGA' or items == 'UAG' or items == 'UAA':
            continue
        translated_codons.append(items)
    v = 0
    sequence_t = ""
    while v < len(translated_codons):
        sequence_t += translated_codons[v]
        v += 1
    print(f"Translated sequence: {sequence_t}\tLength: {len(sequence_t)}")
    print(f"Number of codons in translated sequence: {len(translated_codons)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
