import pymysql
from Persona import Person

class List (object):
    Lista = []

    def Print(self):
        for item in self.Lista:
            print(("DNI: ") + (item.ID))
            print(("Nombre: ") + (item.Name))
            print(("Apellido: ") + (item.Surname) + ("\n"))

    def Insert(self, person):
        self.Lista.append(person)
        db = pymysql.connect(host="localhost", user='root', passwd='', db='test', autocommit=True)
        c = db.cursor(pymysql.cursors.DictCursor)
        c.execute("insert into Persona values('" + person.ID + "', '" + person.Name + "', '" + person.Surname + "')")

    def Delete(self, person):
        db = pymysql.connect(host="localhost", user='root', passwd='', db='test', autocommit=True)
        c = db.cursor(pymysql.cursors.DictCursor)
        c.execute("delete from Persona where DNI = '" + person.ID + "';")

    def Update(self, person):
        db = pymysql.connect(host="localhost", user='root', passwd='', db='test', autocommit=True)
        c = db.cursor(pymysql.cursors.DictCursor)
        c.execute(
            "update Persona set Nombre = '" + person.Name + "', Apellido= '" + person.Surname + "' where DNI = '" + person.ID + "';")