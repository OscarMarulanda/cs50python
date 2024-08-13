class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    student._house = "Restrepo"
    print(student)








if __name__ == "__main__":
    main()

