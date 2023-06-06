normal_list = [1, 2, 3, 4, 5]


class CustomSequence:
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return f"x{index}"


class FunkyBackwards:
    def __reversed__(self):
        return "BACKWARDS"