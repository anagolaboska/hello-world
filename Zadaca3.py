# domasna zadaca 2+ : Da se isprintaat site atributi za zadaden objekt od employee_list.
# zadaca 1
# Da se napravat 2 instanci od klasata Company i 3 instanci od klasata Employee.

# zadaca 2
# Da se napravi sporedba za prosecnite salary costs za sekoja kompanija.

# zadaca 3
# Da se napise metod days_off so koj employee ke ima pravo da bara denovi odmor.
# Pritoa imame annual leave, special circumstances leave, maternity leave, sick days leave.

# zadaca 4
# Da se napise metod promotion so koj employee ke moze da bide unapreden.

# zadaca 5
# Da se napravi klasa Produkt.
# Da se dodadat zadolzitelni atriibuti pri kreiranje na instanca od Produkt: naziv, seriski_broj, cena, tip
# i opcionalen atribut kolicina.

# zadaca 6
# Da se napravi klasa Prodavnica.
# Instancata od prodavnicata, mora da ima: ime, seriski_broj.
# Da se kreira metod dodaj_produkt, koj kje dodava produkti vo prodavnicata,
# so toa sto mora da se proveri dali e od tip Produkt.

# zadaca 7
# Da se kreira klasa Kupuvac.
# Sekoj Kupuvac mora da ima: ime, prezime, dostapni_paricni_sredstva.

# zadaca 8
# Da se kreiraat __str__ metodi za klasite.
# Da se kreira metod pecati_produkti na klasata Prodavnica koj sto kje gi printa site dostapni produkti.

# zadaca 9
#  Da se kreiraat 5 produkti.
# Da se kreiraat 2 prodavnici.
# Da se dodadat produkti vo prodavnicite.
# Da se kreiraat kupuvaci.
# Da se napravi scenario, kupuvacot da kupi produkt od prodavnica. Vo slucaj ako go nema produktot,
# da proba da go kupi produktot od drugata prodavnica.
# Pri kupuvanje na produkt od prodavnica, treba da se izbrise istoit od listata na produkti. Za ova da se koristi
# privaten metod __brisi_produkt.
# Da se vnimava na dostapnite sredstva na kupuvacot.

class Employee:
    def __init__(self, first_name, last_name, email, position=None, company=None, salary=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.position = position
        self.company = company
        self.salary = salary
        self.leave_balance = {
            'annual_leave': 30,
            'special_circumstances_leave': 10,
            'maternity_leave': 60,
            'sick_days_leave': 15
        }

    def accept_offer(self, company, position, salary):
        if not self.company:
            print(f"{self.first_name} {self.last_name} receives a job offer from {company.name} for the position of {position} with a salary of {salary}.")
            self.position = position
            self.salary = salary
            self.company = company
            company.hire(self, position, salary)
        else:
            print(f"{self.first_name} {self.last_name} is already employed at {self.company.name}.")

    def reject_offer(self, company):
        if not self.company:
            print(f"{self.first_name} {self.last_name} rejects the job offer from {company.name}.")
        else:
            print(f"{self.first_name} {self.last_name} cannot reject the offer. Already employed at {self.company.name}.")

    def leave_company(self):
        if self.company:
            print(f"{self.first_name} {self.last_name} leaves {self.company.name}.")
            self.position = None
            self.salary = None
            self.company = None
        else:
            print(f"{self.first_name} {self.last_name} cannot leave a company. Not currently employed.")

    def days_off(self, leave_type, days):
        if leave_type in self.leave_balance and self.leave_balance[leave_type] >= days:
            print(f"{self.first_name} {self.last_name} has been granted {days} days of {leave_type} leave.")
            self.leave_balance[leave_type] -= days
        else:
            print(f"{self.first_name} {self.last_name} does not have enough {leave_type} leave balance.")

    def promotion(self, new_position, new_salary):
        print(f"{self.first_name} {self.last_name} has been promoted to {new_position} with a new salary of {new_salary}.")
        self.position = new_position
        self.salary = new_salary


class Company:
    def __init__(self, name, company_id, address):
        self.name = name
        self.company_id = company_id
        self.address = address
        self.employees = []

    def hire(self, employee, position, salary):
        self.employees.append(employee)

    def send_job_offer(self, employee, position, salary):
        print(f"{self.name} sends a job offer to {employee.first_name} {employee.last_name}.")
        employee.accept_offer(self, position, salary)


employee1 = Employee("Ana", "Golaboska", "ana-atanasoska90@hotmail.com")
employee2 = Employee("Mina", "Janeva", "minajaneva@hotmail.com")
employee3 = Employee("Tina", "Popovska", "tinapopovska@hotmail.com")

companyA = Company("Makedonska", 1, "Kukja")
companyB = Company("Kafana Doma", 2, "Kukja 15678")

companyA.send_job_offer(employee1, "QA Engineer", 80000)
employee1.accept_offer(companyA, "QA Engineer", 80000)

companyA.send_job_offer(employee2, "Developer", 90000)
employee2.reject_offer(companyA)

employee1.leave_company()

companyB.send_job_offer(employee2, "UX Designer", 75000)

valid_salaries_companyA = [employee.salary for employee in companyA.employees if employee.salary is not None]
valid_salaries_companyB = [employee.salary for employee in companyB.employees if employee.salary is not None]

avg_salary_companyA = sum(valid_salaries_companyA) / len(valid_salaries_companyA) if valid_salaries_companyA else 0
avg_salary_companyB = sum(valid_salaries_companyB) / len(valid_salaries_companyB) if valid_salaries_companyB else 0


print(f"Average salary cost for {companyA.name}: ${avg_salary_companyA:.2f}")
print(f"Average salary cost for {companyB.name}: ${avg_salary_companyB:.2f}")

print(vars(employee1))
print(vars(employee2))
print(vars(employee3))

employee1.days_off('annual_leave', 5)
employee2.days_off('sick_days_leave', 3)

employee3.promotion("Senior UX Designer", 90000)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} dollars."

class Store:
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"{product.name} added to {self.name}.")
        else:
            print("Invalid product!")

    def __delete_product(self, product):
        self.products.remove(product)

    def print_products(self):
        print(f"Products in {self.name}:")
        for product in self.products:
            print(f"- {product}")

class Buyer:
    def __init__(self, first_name, last_name, available_funds):
        self.first_name = first_name
        self.last_name = last_name
        self.available_funds = available_funds

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Available funds: {self.available_funds} dollars."

    def buy_product(self, product, store):
        if product in store.products and self.available_funds >= product.price:
            self.available_funds -= product.price
            store._Store__delete_product(product)  # Fix here
            print(f"{self.first_name} bought {product.name} from {store.name}.")
        elif product in store.products and self.available_funds < product.price:
            print(f"{self.first_name} does not have enough funds to buy {product.name}.")
        else:
            print(f"{product.name} is not available in {store.name}.")

product1 = Product("Telefon", 200)
product2 = Product("Klima", 100)
product3 = Product("Televizor", 300)
product4 = Product("XBox", 500)
product5 = Product("Monitor", 1000)

store1 = Store("Neptun", "56789")
store2 = Store("Tehnomarket", "12312")

store1.add_product(product1)
store1.add_product(product2)
store1.add_product(product3)

store2.add_product(product4)
store2.add_product(product5)

buyer1 = Buyer("Ana", "Golaboska", 200)
buyer2 = Buyer("Mina", "Tina", 300)


store1.print_products()
store2.print_products()

buyer1.buy_product(product1, store1)
buyer1.buy_product(product4, store2)

print(buyer1)
print(buyer2)