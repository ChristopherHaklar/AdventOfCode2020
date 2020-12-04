from collections import Counter

class Day2():

    def __init__(self):
        self.input_file = "input.txt"
        self.inputs = []
        self.get_inputs()

    def parse_input(self, i):
        inp = {}
        bounds, letter, password = i.strip().split(" ")

        # cleaning bounds
        bounds = list(map(int, bounds.split("-")))
        assert len(bounds)==2 # assuption: only 2 bounds are provided
        lb, ub = bounds
        assert lb < ub and isinstance(lb, int) and isinstance(ub, int)

        # cleaning letter
        letter = letter.strip(":")
        assert len(letter) == 1 #assuption: only 1 letter is provided

        inp = dict(lb=lb, ub=ub, letter=letter, password=password)
        return inp

    def get_inputs(self):
        f = open(self.input_file, "r")
        for i in f:
            inp = self.parse_input(i)
            self.inputs.append(inp)

    def validate_passwords_1(self):
        valids = 0
        for i in self.inputs:
            pass_counts = Counter(i['password'])
            freq = (pass_counts.get(i['letter'], 0))
            if freq in range(i['lb'], i['ub']+1):
                valids += 1
        print(f"No. of valid passwords (part 1): {valids}")


    def validate_passwords_2(self):
        valids = 0
        for i in self.inputs:
            char_1, char_2 = i['password'][i['lb']-1], i['password'][i['ub']-1]
            if i['letter'] in [char_1, char_2] and char_1 != char_2:
                valids += 1
        print(f"No. of valid passwords (part 2): {valids}")

if __name__ == "__main__":
    d = Day2()
    d.validate_passwords_1()
    d.validate_passwords_2()
