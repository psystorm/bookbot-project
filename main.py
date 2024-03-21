import collections

def word_count(strg):
    return len(strg.split())

def letter_count(strg):
    return collections.Counter(c for word in strg.lower().split() for c in word if c.isalpha())

def book_report(f_name,strg):
    print(f'--- Begin Report of {f_name} ---')
    print(f'Total Word Count: {word_count(strg)}')
    for elem in letter_count(strg).most_common():
        print(f"The '{elem[0]}' character was found {elem[1]} times")
    print(f'--- End Report of {f_name} ---')

def main():
    file_contents = ''
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
    
    book_report(f.name,file_contents)

main()
