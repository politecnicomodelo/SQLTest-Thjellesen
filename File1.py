import pymysql
from Persona import Person
from Base import List

Lista1 = List()

Lista1.Load()

while True:

    Input = input("1 - Add Person\n"
                  "2 - Delete Person\n"
                  "3 - Update Person\n"
                  "4 - Print List\n"
                  "5 - Write in Archive\n"
                  "6 - Exit\n")

    if Input == "1":
        Persona1 = Person()
        Persona1.setID(input("ID "))
        Persona1.setName(input("Name "))
        Persona1.setSurname(input("Surname "))
        Lista1.Insert(Persona1)

    elif Input == "2":
        Lista1.Delete(input("ID "))

    elif Input == "3":
        Persona1.setID (input("ID "))
        Persona1.setName (input("Name "))
        Persona1.setSurname (input("Surname "))
        Lista1.Update(Persona1)

    elif Input == "4":
        Lista1.Print()

    elif Input == "5":
        Lista1.Test()

    elif Input == "6":
        exit()