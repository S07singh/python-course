class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Sudhir", 120000, 841438)
print(p.name,  p.salary, p.pin, p.company)
r = Programmer("Rahul", 120000, 841438)
print(r.name, r.salary, r.pin, r.company)