# forms.py
from django import forms
from account.models import Address

class AddressUserForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['phone', 'province', 'license_plate', 'city', 'postal_code', 'address', 'meli_code']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'input-namefirst-checkout form-control', 'autocomplete': 'off'}),
            'province': forms.TextInput(attrs={'class': 'input-namefirst-checkout form-control', 'autocomplete': 'off'}),
            'license_plate': forms.TextInput(attrs={'class': 'input-namefirst-checkout form-control', 'autocomplete': 'off'}),
            'city': forms.TextInput(attrs={'class': 'input-namefirst-checkout form-control', 'autocomplete': 'off'}),
            'postal_code': forms.TextInput(attrs={'class': 'input-namefirst-checkout form-control', 'autocomplete': 'off'}),
            'address': forms.Textarea(attrs={'class': 'input-namefirst-checkout form-control', 'rows': 4, 'autocomplete': 'off'}),
            'meli_code': forms.TextInput(attrs={'class': 'input-namefirst-checkout form-control', 'autocomplete': 'off'}),
        }
        labels = {
            'phone': 'شماره تلفن',
            'province': 'استان',
            'license_plate': 'پلاک',
            'city': 'شهر',
            'postal_code': 'کد پستی',
            'address': 'آدرس',
            'meli_code': 'کد ملی',
        }

    def clean_meli_code(self):
        meli_code = self.cleaned_data.get('meli_code')
        if meli_code is None:
            raise forms.ValidationError("کد ملی الزامی است.")
        if not meli_code.isdigit() or len(meli_code) != 10:
            raise forms.ValidationError("کد ملی باید ۱۰ رقم و فقط شامل عدد باشد.")
        return meli_code

    def clean_license_plate(self):
        license_plate = self.cleaned_data.get('license_plate')
        if not license_plate:
            raise forms.ValidationError("پلاک الزامی است.")
        return license_plate

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone or len(phone) != 11:
            raise forms.ValidationError("شماره تلفن باید 11 رقم باشد.")
        return phone

    def clean_postal_code(self):
        postal_code = self.cleaned_data.get('postal_code')
        if not postal_code.isdigit() or len(postal_code) < 5:
            raise forms.ValidationError("کد پستی باید شامل حداقل 5 رقم باشد و فقط عدد باشد.")
        return postal_code
