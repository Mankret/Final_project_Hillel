from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    summary = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    id_book_warehouse = models.IntegerField(blank=True, null=True)
    publication_year = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.pk)])

    def __str__(self):
        return self.title



class Order(models.Model):
    STATUS_CHOICE = (
        ('cart', 'Cart'),
        ('ordered', 'Ordered'),
        ('success','Success'),
        ('Fail', 'fail'),
    )

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, max_length=10)
    delivery_adress = models.CharField(max_length=320)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=100, decimal_places=2)

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)