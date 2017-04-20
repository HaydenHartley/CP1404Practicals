class Guitar:
    def __init__(self):
        self.name = ""
        self.year = 0
        self.cost = 0

    def __str__(self):
        return"{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False

    def get_age(self):
        age = 2017 - self.year
        return age
