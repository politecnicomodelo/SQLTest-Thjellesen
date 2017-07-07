import pymysql
from Persona import Person


class List (object):

    Lista = None

    db = None
    c = None

    def __init__(self):
        self.db = pymysql.connect(host="localhost", user='root', passwd='', db='mydb', autocommit=True)
        self.c = self.db.cursor(pymysql.cursors.DictCursor)
        self.Lista = []

    def ReadFile(self):
        with open("Archivo.txt", "r") as File:
            ListaAux = []
            for item in File:
                Persona2 = Person()
                ListaAux = item.split('|')
                Persona2.setID(ListaAux[0])
                Persona2.setName(ListaAux[1])
                Persona2.setSurname(ListaAux[2])
                self.Lista.append(Persona2)

    def Test(self):
        self.c.execute("select Nombre from Persona where DNI = 2")
        print(self.c.fetchall())
        self.c.execute("select Apellido from Persona where DNI = 2")
        print(self.c.fetchall())

    def Insert(self, person):
        self.Lista.append(person)
        self.c.execute("insert into Persona values('"+person.ID+"', '"+person.Name+"', '"+person.Surname+"')")

    def Delete(self, person):
        self.c.execute("delete from Persona where DNI = '"+person+"';")
        for item in self.Lista:
            if item.ID == person:
                self.Lista.remove(item)

    def Update(self, person):
        self.c.execute("update Persona set Nombre = '"+person.Name+"', Apellido= '"+person.Surname+"' where DNI = '"+person.ID+"';")
        for item in self.Lista:
            if item.ID == person.ID:
                item.Name = person.Name
                item.Surname = person.Surname

    def Print(self):
        for item in self.Lista:
            print("DNI: " + item.ID)
            print("Nombre: " + item.Name)
            print("Apellido: " + item.Surname + "\n")

    def Write(self):
        with open("Archivo.txt", "w") as File:
            for item in self.Lista:
                File.write(item.ID + "|")
                File.write(item.Name + "|")
                File.write(item.Surname + "| \n")
