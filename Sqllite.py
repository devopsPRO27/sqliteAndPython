import sqlite3
#create table COMPANY_HIGH
#(
#    ID      INTEGER not null
#        primary key autoincrement,
#    NAME    TEXT    not null,
#    AGE     INT     not null,
#    ADDRESS CHAR(50),
#    SALARY  REAL
#);


class User:
    def __init__(self,id , name ,lastname,age):
        self.id=id
        self.name=name
        self.lastname=lastname
        self.age=age
    def __str__(self):
        return f' {self.id}  {self.name}  {self.age} '

conn = sqlite3.connect(r'C:\Users\hothaifa\Desktop\myfirstDB.db')
print("Opened database successfully")

def printTable(cond=''):
    cursor= conn.execute("SELECT * FROM Users "+cond)
    for row in cursor:
        user2 = User(row[0], row[1], row[2], row[3])
        print(user2)
def insertIntoTable(user):
    conn.execute(f"INSERT INTO Users  VALUES ({user.id},\"{user.name}\",\"{user.lastname}\",{user.age})")
    conn.commit()
    print(f'user {user.name} wa inserted to the Users Table')


user3=User(13,'lidor','seri',41)
insertIntoTable(user3)
printTable('WHERE NAME LIKE "___"')





conn.close()



#id=input("please enter your id")
#name=input("please enter your name")
#lastname=input("please enter your lastname")
#age=input("please enter your age")
#
#user1= User(id,name,lastname,age)
#
#conn.execute(f"INSERT INTO Users (id,name,lastname,age) VALUES({user1.id},\"{user1.name}\",\"{user1.lastname}\",{user1.age})")
#conn.commit()
#print("====================")
#
#cursor=conn.execute('select * from Users ')
##cursor
#for row in cursor:
#    user2=User(row[0],row[1],row[2],row[3])
#    print(user2)
#
#
#


####################
