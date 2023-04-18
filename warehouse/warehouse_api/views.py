from rest_framework import viewsets, permissions, renderers

from warehouse_api.permissions import IsOwnerOrReadOnly
from warehouse_api.models import Book, BookItem, Order, OrderItem, OrderItemBookItem
from warehouse_api.serializers import BookSerializer, OrderSerializer




class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

