from EnglishWords import EnglishWords


class WordsGenerator:
    def __init__(self,dictionary, input_letters=None,mandatory_letter=None, min_size=None):
        self.input_letters = input_letters
        self.mandatory_letter = mandatory_letter
        self.min_size = min_size
        self.english_dict = dictionary
        self.output_words = []


    def valid_jumble(self, word):
        if self.mandatory_letter and (self.mandatory_letter not in word):
            return False

        for char in word:
            if char not in self.input_letters:
                return False
        return True

    def find_words(self, start_char):
        words = []
        for word in self.english_dict[start_char]:
            if self.valid_jumble(word):
                if len(word) >= self.min_size:
                    words.append(word)
        return words

    def generate(self):
        for char in self.input_letters:
            self.output_words += self.find_words(char)
        self.display_output()


    def display_output(self):
        print()
        print(f"Input Letters: {self.input_letters}")
        print(f"Mandatory Letter: {self.mandatory_letter}")
        print(f"Minimun word size: {self.min_size}")
        print("\nOutput list is")
        print(f"length {len(self.output_words)}\n")
        for word in self.output_words:
            print(word)
