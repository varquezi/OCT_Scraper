from typing import List

class Date:
    def __init__(self, date: str):
        self.year = int(date[:4])
        self.month = int(date[5:7])
        self.day = int(date[8:])

    def __str__(self):
        return "{:04d}/{:02d}/{:02d}".format(self.year, self.month, self.day)


class Degree:
    def __init__(self, name: str, date: Date, place: str):
        self.name = name
        self.date = date
        self.place = place
    def __str__(self):
        return "[{}] {} @ {}".format(self.date, self.name, self.place)


class Teacher:
    def __init__(self, id: int, firstName: str, midName: str, lastName: str):
        self.id = id
        self.firstName = firstName
        self.midName = midName
        self.lastName = lastName
        self.fullName = "{} {} {}".format(firstName, midName, lastName)
        self.degrees = {}

    def addDegree(self, degree: Degree):
        self.degrees.setdefault(degree.place, []).append({"date": degree.date,"name": degree.name})

    def __str__(self):
        rep = "[{}] {}".format(self.id, self.fullName)
        for place in self.degrees:
            rep += "\n\t{}".format(place)
            for degree in self.degrees[place]:
                rep += "\n\t\t[{}] {}".format(degree["date"], degree["name"])
        return rep