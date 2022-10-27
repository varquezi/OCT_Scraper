class Degree:
    def __init__(self, name: str, date: tuple, place: str):
        self.name = name
        self.date = {"year":date[0], "month":date[1],"day":date[2]}
        self.place = place
    def __str__(self):
        return "[{}] {} @ {}".format(self.date, self.name, self.place)


class Teacher:
    def __init__(self, id: int, firstName: str, lastName: str):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.degrees = []

    def addDegree(self, degree: Degree):
        self.degrees.append({"place": degree.place, "date": degree.date,"name": degree.name})

    def __str__(self):
        rep = "[{}] {} {}".format(self.id, self.firstName, self.lastName)
        for degree in self.degrees:
            rep += "\n\t{}".format(degree["place"])
            rep += "\n\t\t[{:04d}/{:02d}/{:02d}] {}".format(degree["date"]["year"], degree["date"]["month"], degree["date"]["day"], degree["name"])
        return rep