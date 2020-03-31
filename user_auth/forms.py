from django import forms
class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)
    email = forms.EmailField(label='Email')

    # write validator
