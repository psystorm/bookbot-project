
def word_count(strg):
    return len(strg.split())

def letter_count(strg):
    lc = {}
    words = strg.lower().split()
    for word in words:
        for letter in word:
            if letter in lc:
                lc[letter] += 1
            else:
                lc[letter] = 1
    return lc

def main():
    file_contents = ''
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
    print(word_count(file_contents))
    print(letter_count(file_contents))

main()
