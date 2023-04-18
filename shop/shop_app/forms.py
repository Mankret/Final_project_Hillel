from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput
# from shop_app.models import Order

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username',
                                         'style': 'width: 300px;',
                                         'class': 'form-control'
                                         }),
                    }



class OrderForm(forms.ModelForm):
    pass

# class AddToCartForm(forms.Form):
#     book_id = forms.IntegerField(widget=forms.HiddenInput())