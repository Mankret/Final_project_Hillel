from django.urls import path, include
from rest_framework.routers import DefaultRouter
from warehouse_api import views


router = DefaultRouter()
router.register(r'book', views.BookViewSet, basename="book")
router.register(r'order', views.OrderViewSet, basename="order")
# router.register(r'comments', views.CommentViewSet, basename="comment")


urlpatterns = [
    path('', include(router.urls)),
]