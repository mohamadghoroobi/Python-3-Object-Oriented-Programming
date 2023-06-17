class Node:
    def __init__(self, tag_name, parent = None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return self.tag_name + ": " + self.text
        else:
            return self.tag_name


class Parser:
    def __init__(self, parse_string):
        self.pase_string = parse_string
        self.root = None
        self.current_node = None

        self.state = FirstTag()

        def process(self, remaining_string):
            remaining = self.state.process(remaining_string, self)
            if remaining:
                self.process(remaining)

        def start(self):
            self.process(self.parse_string)