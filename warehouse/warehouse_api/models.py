from django.db import models
# from shop.shop_app.models import Order as ShopOrder




class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    summary = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publication_year = models.DateField(blank=True, null=True)


class BookItem(models.Model):
    book_id = models.OneToOneField(Book, on_delete=models.CASCADE)



class Order(models.Model):
    STATUS_CHOICE = (
        ('in_work', 'In work'),
        ('success', 'Success'),
        ('Fail', 'fail'),
    )

    user_email = models.EmailField()
    status = models.CharField(choices=STATUS_CHOICE, max_length=10)
    delivery_adress = models.CharField(max_length=320)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=100, decimal_places=2)
    order_id_in_shop = models.IntegerField(blank=True, null=True)
    # order_in_shop = models.ForeignKey(ShopOrder, on_delete=models.CASCADE, related_name='warehouse_orders')


class OrderItem(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    book_warehouse_id = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class OrderItemBookItem(models.Model):
    order_item_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    book_item_id = models.OneToOneField(Book, on_delete=models.CASCADE)