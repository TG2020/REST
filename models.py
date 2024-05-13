import os
import json


class Books:
    def __init__(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "books.json"))
        try:
            with open(file_path, "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []

    def all(self):
        return self.books

    def get(self, nr):
        return self.books[nr]

    def create(self, data):
        self.books.append(data)
        self.save_all()

    def delete(self, nr):
        book = self.get(nr)
        if book:
            self.books.remove(book)
            self.save_all()
            return True
        return False

    def update(self, nr, data):
        book = self.get(nr)
        if book:
            index = self.books.index(book)
            self.books[index] = data
            self.save_all()
            return True
        return False

    def save_all(self):
        pass


books = Books()
