import pymysql
from Persona import Person

class List (object):
    Lista = None

    db = None
    c = None

    def __init__ (self):
        self.db = pymysql.connect(host="localhost", user='root', passwd='', db='mydb', autocommit=True)
        self.c = self.db.cursor(pymysql.cursors.DictCursor)
        self.Lista = []

    def Load (self):
        with open("Archivo.txt", "r") as Archive:


    def Print(self):
        for item in self.Lista:
            print(("DNI: ") + (item.ID))
            print(("Nombre: ") + (item.Name))
            print(("Apellido: ") + (item.Surname) + ("\n"))

    def Insert(self, person):
        self.Lista.append(person)
        self.c.execute("insert into Persona values('" + person.ID + "', '" + person.Name + "', '" + person.Surname + "')")

    def Delete(self, person):
        self.c.execute("delete from Persona where DNI = '" + person + "';")
        for item in self.Lista:
            if item.ID == person:
                self.Lista.remove(item)

    def Update(self, person):
        self.c.execute("update Persona set Nombre = '" + person.Name + "', Apellido= '" + person.Surname + "' where DNI = '" + person.ID + "';")

    def Test (self):
        with open("Archivo.txt", "a") as Archive:
            for item in self.Lista:
                Archive.write(item.ID + "|")
                Archive.write(item.Name + "|")
                Archive.write(item.Surname + "| \n")