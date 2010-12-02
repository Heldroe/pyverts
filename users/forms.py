from django import forms
from django.core.exceptions import ValidationError

class SignupForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50, required=True,
        error_messages={'required': 'Name is missing',
                        'min_length': 'Minimal length : 2 chars',
                        'max_length': 'Maximal length : 50 chars'})
    password = forms.CharField(min_length=4, required=True,
        error_message={'required': 'Password needed',
                       'min_length': '4 chars or more please'})
    password2 = forms.CharField(min_length=4, required=True,
        error_message={'required': 'Password x2 needed',
                       'min_length': '4 chars or more please'})

