from django import forms
from django.core.exceptions import ValidationError
from .models import MyUser  # فرض بر این است که مدل شما MyUser نام دارد

class UserLoginForm(forms.Form):
    phone = forms.CharField(
        label='phone',
        max_length=12,
        widget=forms.NumberInput(
            attrs={'class': "form-control", 'autocomplete': 'off'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'password-input', 'autocomplete': 'off'}
        )
    )

class UserRegisterForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': "number-email-input", 'autocomplete': 'off'}
        )
    )
    last_name = forms.CharField(
        label='نام خانوادگی',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': "number-email-input", 'autocomplete': 'off'}
        )
    )
    phone = forms.CharField(
        label='شماره تلفن',
        max_length=12,
        widget=forms.TextInput(
            attrs={'class': "number-email-input", 'autocomplete': 'off'}
        )
    )
    email = forms.EmailField(
        label="ایمیل",
        max_length=250,
        widget=forms.EmailInput(
            attrs={'class': 'number-email-input', 'autocomplete': 'off'}
        )
    )
    pass1 = forms.CharField(
        label="پسورد",
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'class': 'password-input', 'autocomplete': 'off'}
        )
    )
    pass2 = forms.CharField(
        label="تکرار کلمه عبور",
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'class': 'password-input', 'autocomplete': 'off'}
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")
        pass1 = cleaned_data.get("pass1")
        pass2 = cleaned_data.get("pass2")

        # Check if passwords match
        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError("پسورد ها یکسان نمی باشند.")

        # Check if email is unique
        if MyUser.objects.filter(email=email).exists():
            self.add_error('email', "این ایمیل قبلاً استفاده شده است.")

        # Check if phone number is unique
        if MyUser.objects.filter(phone=phone).exists():
            self.add_error('phone', "این شماره تلفن قبلاً استفاده شده است.")

        return cleaned_data
