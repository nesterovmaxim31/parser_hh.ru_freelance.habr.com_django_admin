from django import forms
from .models import Vacanci, Vacanci_2


class Vacanci_Forms(forms.ModelForm):
    class Meta:
        model = Vacanci
        fields = ('Title', 'Link', 'Salary', 'No_resume', 'First', 'Company', 'Date', 'Address')
        widgets = {'Title': forms.TextInput, 'Company': forms.TextInput}


class Vacanci_Forms_2(forms.ModelForm):
    class Meta:
        model = Vacanci_2
        fields = ('Title', 'Link', 'Price', 'Number_of_otkliks', 'Number_of_vues')
        widgets = {'Title': forms.TextInput, 'Price': forms.TextInput, 'Number_of_otkliks': forms.TextInput,
                   'Number_of_vues': forms.TextInput}
