from django import forms

class InputForm(forms.Form):
    input_field1 = forms.CharField(label='Latitude ')
    input_field2 = forms.CharField(label='Longitude ')
    # receive_newsletter = forms.BooleanField(label='')

