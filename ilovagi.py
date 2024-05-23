class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show_title(self):
        return f"title: {self.title}"
    def show_author(self):
        return f"author: {self.author}"
    def show_title_author(self):
        return f"{self.title} _ {self.author}"

my_book = Book("Shohnoma", "Abulqosimi Firdavsi")
print(my_book.show_title())
print(my_book.show_author())
print(my_book.show_title_author())





