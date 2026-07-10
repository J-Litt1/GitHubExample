class Students:
    def __init__(self, ID, firstName, surname, age, grade):
        self.__ID = ID
        self.firstName = firstName
        self.surname = surname
        self.__age = age
        self.__grade = grade

    def birthday(self):
        self.__age += 1
        print("Happy birthday!")

    def get_ID(self):
        return self.__ID

    def get_age(self):
        return self.__age

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if (grade < 0) or (grade > 100):
            print("Didn't set - grade must be 0-100")
        else:
            self.__grade = grade

    def greeting(self):
        print("Hello, I'm " + self.firstName + " " + self.lastName + " and I'm a student")


class SchoolStaff:
    def __init__(self, firstName, surname, age):
        self.firstName = firstName
        self.surname =surname
        self.__age = age

    def birthday(self):
        self.__age += 1
        print("Happy birthday!")

    def get_age(self):
        return self.__age


class Teachers(SchoolStaff):
    def __init__(self, firstName, surname, age, title):
        SchoolStaff.__init__(self, firstName, surname, age)
        self.title = title

    def greeting(self):
        print("Hello, my name is " + self.title + " " + self.surname)


class Cleaners(SchoolStaff):
    def __init__(self, firstName, surname, age):
        SchoolStaff.__init__(self, firstName, surname, age)
        
    def greeting(self):
        print("Hello, my name is " + self.firstName + " " + self.surname + " and I'm a cleaner")


def main():
    test = Teachers("James", "Littlemore", 22, "Mr")
    test.greeting()


main()