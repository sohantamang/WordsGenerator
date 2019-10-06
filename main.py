from EnglishWords import EnglishWords
from WordsGenerator import WordsGenerator

# Start here
input = "tholufg"
required_letter = "g"
filename = "words_long.txt"
MIN_LENGTH = 4

eng_dict = EnglishWords(filename)
words_gen = WordsGenerator(dictionary=eng_dict.dict_hash,input_letters=input,\
 mandatory_letter=required_letter, min_size=MIN_LENGTH)
words_gen.generate()
