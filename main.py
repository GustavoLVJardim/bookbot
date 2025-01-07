def counting_words():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)

def counting_characters():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read().lower()
        
        dict_characters = {}
        dict_anything = {}
        
        for char in file_contents:
            if char.isalpha():
                if char in dict_characters:
                    dict_characters[char] += 1
                else:
                    dict_characters[char] = 1
            else:
                if char in dict_anything:
                    dict_anything[char] += 1
                else:
                    dict_anything[char] = 1
        
        return dict_characters

def main():
    print("---Begin report of books/frankenstein.txt---")
    print(f"{counting_words()} words in the document")
    
    for k,v in counting_characters().items():
        print(f"The letter {k} character was found {v} times")

if __name__ == '__main__':
    main()