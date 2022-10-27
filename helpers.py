class Degree:
    def __init__(self, name: str, date: tuple, place: str):
        self.name = name
        self.date = {"year":date[0], "month":date[1],"day":date[2]}
        self.place = place
    def __str__(self):
        return "[{}] {} @ {}".format(self.date, self.name, self.place)


class Teacher:
    def __init__(self, id: int, firstName: str, midName: str, lastName: str):
        self.id = id
        self.firstName = firstName
        self.midName = midName
        self.lastName = lastName
        self.degrees = {}

    def addDegree(self, degree: Degree):
        self.degrees.setdefault(degree.place, []).append({"date": degree.date,"name": degree.name})

    def __str__(self):
        rep = "[{}] {} {} {}".format(self.id, self.firstName, self.midName, self.lastName)
        for place in self.degrees:
            rep += "\n\t{}".format(place)
            for degree in self.degrees[place]:
                rep += "\n\t\t[{:04d}/{:02d}/{:02d}] {}".format(degree["date"]["year"], degree["date"]["month"], degree["date"]["day"], degree["name"])
        return rep