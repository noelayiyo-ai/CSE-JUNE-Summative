from .models import Registration
from django import forms


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'Date_of_Birth':forms.DateInput(attrs={'type':'date'}),
            'Date_of_joining_Settlement_camp':forms.DateInput(attrs={'type':'date'})
        }
