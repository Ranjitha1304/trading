# mainapp/forms.py
from django import forms
import re

CITIES = [
    ("mumbai", "Mumbai"),
    ("delhi", "Delhi"),
    ("bangalore", "Bangalore"),
    ("chennai", "Chennai"),
    ("kolkata", "Kolkata"),
]

NAME_REGEX = re.compile(r"^[A-Za-z\s]{3,15}$")
PHONE_REGEX = re.compile(r"^\d{10}$")
PINCODE_REGEX = re.compile(r"^\d{6}$")

class PartnerForm(forms.Form):
    name = forms.CharField(
        max_length=15,
        min_length=3,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Your Name"}),
        label="Your Name"
    )
    phone = forms.CharField(
        max_length=10,
        min_length=10,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Phone Number"}),
        label="Phone Number"
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "E-Mail Id"}),
        label="E-Mail Id"
    )
    city = forms.ChoiceField(choices=CITIES, required=True, label="Select a City")
    pincode = forms.CharField(
        max_length=6,
        min_length=6,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Pin Code"}),
        label="Pin Code"
    )

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if not NAME_REGEX.match(name):
            raise forms.ValidationError("Name must be 3-15 letters only.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()
        if not PHONE_REGEX.match(phone):
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone

    def clean_pincode(self):
        pin = self.cleaned_data.get("pincode", "").strip()
        if not PINCODE_REGEX.match(pin):
            raise forms.ValidationError("Pin code must be exactly 6 digits.")
        return pin



import re
from django import forms

NAME_REGEX = re.compile(r"^[A-Za-z\s]{3,15}$")
PHONE_REGEX = re.compile(r"^\d{10}$")

class RegisterForm(forms.Form):
    name = forms.CharField(label="Name", max_length=15, min_length=3)
    mobile = forms.CharField(label="Mobile No", max_length=10, min_length=10)
    email = forms.EmailField(label="E-mail Id")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if not NAME_REGEX.match(name):
            raise forms.ValidationError("Name must be 3-15 letters only.")
        return name

    def clean_mobile(self):
        m = self.cleaned_data.get("mobile", "").strip()
        if not PHONE_REGEX.match(m):
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return m

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned


class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail Id")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
