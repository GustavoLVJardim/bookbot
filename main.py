import sys
from stats import counting_words

def counting_characters():
    with open(sys.argv[1]) as f:
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
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f" Found {counting_words()} total words")
    print()
    print("--------- Character Count -------")
    
    for k,v in counting_characters().items():
        print(f"{k}: {v}")
    

    
if __name__ == '__main__':
    main()