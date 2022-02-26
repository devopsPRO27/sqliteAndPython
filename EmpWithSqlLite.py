class Employee:
    def __init__(self, id, name, address, salary):
        self.id = id
        self.name = name
        self.address = address
        self.salary = salary

    def __str__(self):
        return f'{self.id} {self.name} {self.address} {self.salary} '


import sqlite3

conn = sqlite3.connect(r'C:\Users\hothaifa\Desktop\myfirstDB.db')


def printEmp(cond=""):
    hodi = conn.execute('SELECT * FROM Employees ')
    for row in hodi:
        temp = Employee(row[0], row[1], row[2], row[3])
        print(temp)


def insertEmp(emp):
    conn.execute(f'INSERT INTO Employees VALUES({emp.id},\"{emp.name}\",\"{emp.address}\",{emp.salary})')
    conn.commit()


printEmp()
emp1 = Employee(1, 'name1', 'telaviv', 5501)
emp2 = Employee(2, 'name2', 'telaviv', 5502)
emp3 = Employee(3, 'name3', 'telaviv', 5503)
insertEmp(emp1)
insertEmp(emp2)
insertEmp(emp3)
emp1 = Employee(4, 'name1', 'telaviv', 5504)
emp2 = Employee(5, 'name2', 'telaviv', 5506)
emp3 = Employee(6, 'name3', 'telaviv', 5507)
insertEmp(emp1)
insertEmp(emp2)
insertEmp(emp3)
emp1 = Employee(7, 'name1', 'telaviv', 5508)
emp2 = Employee(8, 'name2', 'telaviv', 5509)
emp3 = Employee(9, 'name3', 'telaviv', 5510)

# insertEmp(emp1)
# insertEmp(emp2)
# insertEmp(emp3)
