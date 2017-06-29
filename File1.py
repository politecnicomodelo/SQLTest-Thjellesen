import pymysql

db =pymysql.connect (host = "localhost", user = 'root', passwd = 'alumno', db = 'mydb', autocommit = True)

c = db.cursor(pymysql.cursors.DictCursor)

def Insert(ID,Name,Surname):
    c.execute("insert into Persona values('"+ID+"', '"+Name+"', '"+Surname+"')")

def Delete(ID):
    c.execute("delete from Persona where DNI = '"+ID+"';")

def Update(ID,Name,Surname):
    c.execute("update Persona set Nombre = '"+Name+"', Apellido= '"+Surname+"' where DNI = '"+ID+"';")

while True:
    Input = input("1 - Add Person\n"
                  "2 - Delete Person\n"
                  "3 - Update Person\n"
                  "4 - Exit\n")

    if Input == "1":
        ID = input("ID ")
        Name = input("Name ")
        Surname = input("Surname ")
        Insert(ID,Name,Surname)

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
