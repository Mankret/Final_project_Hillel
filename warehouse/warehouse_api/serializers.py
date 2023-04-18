from rest_framework import serializers
from .models import Book, BookItem, Order, OrderItem, OrderItemBookItem


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BookItem
        fields = ['book']


class OrderItemBookItemSerializer(serializers.ModelSerializer):
    book_item = BookItemSerializer()

    class Meta:
        model = OrderItemBookItem
        fields = ['book_item']


class OrderItemSerializer(serializers.ModelSerializer):
    book_warehouse = BookSerializer()
    order_item_book_items = OrderItemBookItemSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = ['book_warehouse', 'quantity', 'price', 'order_item_book_items']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['user_email', 'status', 'delivery_adress', 'created_at', 'total_price', 'order_items']
