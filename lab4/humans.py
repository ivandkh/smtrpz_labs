class Human():

    name: str

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "Hi, I'm %s." % self.name


class Policeman(Human):
    def __repr__(self):
        return "Hello! I'm officer %s." % self.name


class Firefighter(Human):
    def __repr__(self):
        return "I'm %s. This is fine." % self.name
