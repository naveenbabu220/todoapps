from django import forms
from .models import Jag,Todo


class Ja(forms.ModelForm):
    class Meta:
        model = Jag
        fields = '__all__'
        widgets = {
            'dob': forms.SelectDateWidget,
            'end_time': forms.SelectDateWidget
        }
