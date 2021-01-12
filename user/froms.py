from .models import User
from django import forms


class Ufr(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
