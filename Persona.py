class Person (object):
    ID = None
    Name = None
    Surname = None

    def setID(self, id):
        self.ID = str(id)

    def setName(self, name):
        self.Name = str(name)

    def setSurname(self, surname):
        self.Surname = str(surname)