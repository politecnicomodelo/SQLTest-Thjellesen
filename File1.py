import pymysql
from .Persona import Person

db =pymysql.connect (host = "localhost", user = 'root', passwd = '1', db = 'test', autocommit = True)

c = db.cursor(pymysql.cursors.DictCursor)

Persona1 = Person()

def Insert(Persona1):
    c.execute("insert into Persona values('"+Persona1.ID+"', '"+Persona1.Name+"', '"+Persona1.Surname+"')")

def Delete(Persona1):
    c.execute("delete from Persona where DNI = '"+ID+"';")

def Update(Persona1):
    c.execute("update Persona set Nombre = '"+Name+"', Apellido= '"+Surname+"' where DNI = '"+ID+"';")

while True:
    Input = input("1 - Add Person\n"
                  "2 - Delete Person\n"
                  "3 - Update Person\n"
                  "4 - Exit\n")

    if Input == "1":
        Persona1.setID(input("ID "))
        Persona1.setName(input("Name "))
        Persona1.setSurname(input("Surname "))
        Insert(Persona1.ID,Persona1.Name,Persona1.Surname)

    elif Input == "2":
        ID = input("ID ")
        Delete(ID)

    elif Input == "3":
        ID = input("ID ")
        Name = input("Name ")
        Surname = input("Surname ")
        Update(ID,Name,Surname)

    elif Input == "4":
        exit()
