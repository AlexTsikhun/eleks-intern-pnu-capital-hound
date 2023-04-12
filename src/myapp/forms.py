from django import forms

class InputForm(forms.Form):
    input_field1 = forms.CharField(label='Latitude ', 
                                   widget=forms.TextInput(attrs={'class': 'my-input-class1'}))
    input_field2 = forms.CharField(label='Longitude ',  
                                   widget=forms.TextInput(attrs={'class': 'my-input-class2'}))
    # receive_newsletter = forms.BooleanField(label='')

