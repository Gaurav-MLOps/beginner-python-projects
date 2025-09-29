 


























class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)

    def list_books(self):
        return [f"{b.title} by {b.author}" for b in self.collection]


library = Library("New York Public Library")

book1 = Book("Harry Potter...", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")

library.add_book(book1)
library.add_book(book2)

print(library.name)
for book in library.list_books():
    print(book)




























class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


company = Company("Krusty Krabs")

company.add_employee("Eugene", "Manager")
company.add_employee("Spongebob", "Cook")
company.add_employee("Squidward", "Cashier")

for employee in company.list_employees():
    print(employee)


































































































































