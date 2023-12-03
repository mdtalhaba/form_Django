from django import forms

class djangoForm(forms.Form) :
    name = forms.CharField()
    email = forms.EmailField()
    date = forms.DateField()
    CHOICE = [('large', 'Large'), ('medium', 'Medium'), ('small', 'Small')]
    size = forms.ChoiceField(choices=CHOICE)
    image = forms.FileField()