
class EnglishWords:
    def __init__(self,filename=None):
        self.filename = filename
        self.dict_hash = {}
        with open(filename) as input:
            for _, line in enumerate(input):
                line = line.rstrip()
                key = line[0]
                if key in self.dict_hash:
                    self.dict_hash[key].append(line)
                else:
                    self.dict_hash[key] = [line]
