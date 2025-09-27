from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        return 3.12 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, width):
        self.width = width
    
    def area(self):
        return self.width ** 2

class Triangle(Shape):
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 1/2 * (self.width * self.height)
    

shapes = [Circle(4), Square(5), Triangle(6, 7)]

for Shape in shapes:
    print(f"{Shape.area()}cm²")  


























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






























class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __gt__(self, other):  
        return self.num_pages < other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title

        elif key == "author":
            return self.author
        
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' not found"
        
book1 = Book("The Hobbit", "J.R.R Tolkien", 310)        
book2 = Book("Harry Potter", "J.K. Rowling", 233)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1['title'])
print(book1['author'])
print(book1['num_pages'])
print(book1['aduio'])




























class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be grater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be grater than zero")

rectangle = Rectangle(3, 4)

rectangle.width = 5 
rectangle.height = 6
 
print(rectangle.width)
print(rectangle.height)













































































