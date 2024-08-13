import random

class Hat:

    houses = ["Montes", "Villa Alsacia", "Muzú", "Bosa"]
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
