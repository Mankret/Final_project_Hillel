from django.urls import path
from . import views
# from .views import add_to_cart


urlpatterns = [
    path('', views.HomeShopView.as_view(), name='home'),
    path('shop/<int:pk>/book', views.BookDetailView.as_view(), name='book-detail'),
    # path('add/', add_to_cart, name='add_to_cart'),
    ]