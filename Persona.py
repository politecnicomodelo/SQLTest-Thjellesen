class Person (object):
    ID = ''
    Name = ''
    Surname = ''

    def setID(self, id):
        self.ID = int(id)

    def setName(self, name):
        self.Name = str(name)

    def setSurname(self, surname):
        self.Surname = str(surname)