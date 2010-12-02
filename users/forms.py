from django import forms
from django.core.exceptions import ValidationError

class SignupForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50, required=True,
        error_messages={'required': 'Name is missing',
                        'min_length': 'Minimal length : 2 chars',
                        'max_length': 'Maximal length : 50 chars'})
    password = forms.CharField(min_length=4, required=True,
                               widget=forms.PasswordInput,
        error_messages={'required': 'Password needed',
                       'min_length': '4 chars or more please'})
    password2 = forms.CharField(min_length=4, required=True,
                                widget=forms.PasswordInput,
        error_messages={'required': 'Password x2 needed',
                       'min_length': '4 chars or more please'})

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get("name")
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password and password2:
            if password != password2:
                msg = 'Passwords must be the same'
                self._errors["password"] = self.error_class([msg])
                self._errors["password2"] = self.error_class([msg])

                del cleaned_data["password"]
                del cleaned_data["password2"]
        return cleaned_data

