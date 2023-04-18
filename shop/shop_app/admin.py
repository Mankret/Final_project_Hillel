from django.contrib import admin
from shop_app.models import Book, Order, OrderItem

admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderItem)