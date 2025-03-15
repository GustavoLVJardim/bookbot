import sys

def counting_words():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)
    

def relatory(dict_words):
    pass

