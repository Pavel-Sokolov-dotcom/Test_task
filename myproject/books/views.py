import logging
from django.shortcuts import render
from .models import Book

# Получаем экземпляр логгера
logger = logging.getLogger(__name__)


def book_list(request):
    try:
        books = Book.objects.all()
        logger.info(f'Выведено {books.count()} книг')
    except Exception as e:
        logger.error(f'Ошибка получения списка кнги {e}')
        books = []
    
    return render(request, 'book_list.html', {'books': books})
