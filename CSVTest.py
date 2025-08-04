import csv
class Employee:
    def __init__(self, name, title, a):
        self.name = name
        self.title = title
        self.a = a
employees = []
with open('Planets.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        employees.append(Employee(row['name'], row['mass'], row['moons']))
print(employees)