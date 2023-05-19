class BaseClass:
    num_base_class = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_class += 1


class LeftSubclass(BaseClass):
    num_left_class = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Left Subclass")
        self.num_left_class += 1
