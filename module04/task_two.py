import os
import string 

def count_words(filename):
    #find the path of py file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    try:
        # Open/Read/Close
        FILE_o = open(file_path)
        raw_data = FILE_o.read()
        FILE_o.close()
        # Remove punctuation
        translator = str.maketrans('','',string.punctuation)
        cleantext = raw_data.translate(translator)
        # Split words into a list
        wordList_fromtxt = str.split(cleantext)
        # directly count the word number by len of list
        return len(wordList_fromtxt)
        
    except FileNotFoundError:
        print("File Path doesn't exist.")
        return None

word_count_num = count_words("The_Zen_of_Python.txt")

print(f"The file counts as {word_count_num} words.")