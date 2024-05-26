from django import forms
from .models import User
class UserRegistrationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'почта'}
        )
    )
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите имя целиком'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'пароль'}
        )
    )


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'почта'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'пароль'}
        )
    )

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email','image']
        widgets = {'full_name': forms.TextInput(attrs={'placeholder':'Фамилия, имя, отечество'},),
                   'email': forms.EmailInput(attrs={'placeholder':'Пример: User@mail.ru'})}