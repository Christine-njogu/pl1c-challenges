import random
import string
import sys

"""
Notes:
- Very good!
"""

def main():
    files = [f"file_{''.join(random.choices(string.ascii_lowercase, k=6))}.pdf" for _ in range(100)]
    # files that have been completely processed
    processed = dict(
        zip(
            random.choices(files, k=10),
            random.choices(range(1, 100), k=10)
        )
    )
    processed_set = set(processed)
    # files currently processing
    processing = random.choices(list(set(files).difference(processed.keys())), k=15)
    processing_set = set(processing)
    # files yet to be processed
    processed_processing_set = processed_set.union(processing_set)
    files_set = set(files)
    unprocessed_set = files_set.difference(processed_processing_set)
    print(f"\nUnprocessed file names:\n {unprocessed_set}")
    print("\nProcessed files with value greater than 50:")
    print("File\t\t\t\t\t\tName")
    for key, value in processed.items():
        if value > 50:
            print(f"{key}\t\t\t\t{value}")


if __name__ == "__main__":
    sys.exit(main())
