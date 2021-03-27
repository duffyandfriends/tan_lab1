from django import forms

class Name_Form(forms.Form):
    name_input = forms.CharField(label='Name:', max_length=50)
