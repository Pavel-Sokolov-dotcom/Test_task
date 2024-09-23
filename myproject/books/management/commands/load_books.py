import csv
from django.core.management.base import BaseCommand
from books.models import Book
import os

class Command(BaseCommand):
    help = 'Load books from a CSV file into the database'
    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(__file__), 'books.csv')
        # Контекстный менеджер открывает файл, цикл перебирает файл и добавляет данные в БД
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            books = []
            for row in reader:
                book = Book(
                    title=row['title'],
                    author=row['author'],
                    published_date=row['published_date']
                )
                books.append(book)
            Book.objects.bulk_create(books)
            self.stdout.write(self.style.SUCCESS(f'В базу данных добавлено {len(books)} записей'))