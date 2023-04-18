from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect

from django.views import generic
from django.urls import reverse_lazy

from shop_app.models import Book, Order, OrderItem
from shop_app.forms import RegisterForm



User = get_user_model()

class HomeShopView(generic.ListView):
    model = Book
    # paginate_by = 3
    template_name = 'home.html'

class RegisterFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=user.username, password=form.cleaned_data.get('password1'))
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class UserProfileView(generic.DetailView):
    model = User
    template_name = 'registration/profile.html'


class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = 'registration/update_profile.html'
    fields = ['username', 'email']
    success_url = reverse_lazy('home')
    success_message = "Profile success update"

    def get_object(self, queryset=None):
        user = self.request.user
        return


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'shop/book_detail.html'

# def add_to_cart(request):
#     if request.method == 'POST':
#         form = AddToCartForm(request.POST)
#         if form.is_valid():
#             book_id = form.cleaned_data['book_id']
#             book = Book.objects.get(id=book_id)
#             user = request.user
#             order, created = Order.objects.get_or_create(user_id=user, status='cart')
#             order_item, created = OrderItem.objects.get_or_create(order_id=order, book_id=book)
#             order_item.quantity += 1
#             order_item.save()
#             return redirect('cart_shop')
#     else:
#         form = AddToCartForm()
#     return render(request, 'shop/add_to_cart.html', {'form': form})