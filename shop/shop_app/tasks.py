import requests
from celery import shared_task
from shop_app.models import Book
from django.core.mail import send_mail


@shared_task
def sending_mail(email, message):
    send_mail(
        'Reminder',
        f'{message}',
        'admin@admin.com',
        [email]
    )
    return 'Done'

@shared_task
def database_synchronization():
    response = requests('http://warehouse:8001/book')
    data = response.json()

    for book_from_warehouse in data['results']:

        Book.objects.create(title=book_from_warehouse['title'],
                            author=book_from_warehouse['author'],
                            summary=book_from_warehouse['summary'],
                            price=book_from_warehouse['price'] ,
                            quantity=book_from_warehouse['quantity'] ,
                            id_book_warehouse=book_from_warehouse['id'] ,
                            publication_year=book_from_warehouse['publication_year'])
    send_mail(
        'ok',
        'new book added',
        'admin@admin.com',
        ['admin@admin.com']
    )
    return 'Done'

