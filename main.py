import collections

def word_count(strg):
    return len(strg.split())

def letter_count(strg):
    return collections.Counter(c for word in strg.lower().split() for c in word)

def main():
    file_contents = ''
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
    print(word_count(file_contents))
    print(letter_count(file_contents))

main()
