import pymysql
from Persona import Person
from Base import List

Persona1 = Person()
Lista1 = List()

while True:
    Input = input("1 - Add Person\n"
                  "2 - Delete Person\n"
                  "3 - Update Person\n"
                  "4 - Print List\n"
                  "5 - Exit\n")

    if Input == "1":
        Persona1.setID(input("ID "))
        Persona1.setName(input("Name "))
        Persona1.setSurname(input("Surname "))
        Lista1.Insert(Persona1)

    elif Input == "2":
        Persona1.setID (input("ID "))
        Lista1.Delete(Persona1)

    elif Input == "3":
        Persona1.setID (input("ID "))
        Persona1.setName (input("Name "))
        Persona1.setSurname (input("Surname "))
        Lista1.Update(Persona1)

    elif Input == "4":
        Lista1.Print()

    elif Input == "5":
        exit()