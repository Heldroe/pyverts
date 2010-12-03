# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import Profile

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
                msg = 'Les mots de pass doivent être les mêmes'
                self._errors["password"] = self.error_class([msg])
                self._errors["password2"] = self.error_class([msg])
            if User.objects.filter(username=cleaned_data.get("name")) :
                msg = 'Cet utilisateur existe déjà'
                self._errors["name"] = self.error_class([msg])
#                del cleaned_data["password"]
#                del cleaned_data["password2"]
        return cleaned_data

class LoginForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50, required=True,
        error_messages={'required': 'Name is missing',
                        'min_length': 'Minimal length : 2 chars',
                        'max_length': 'Maximal length : 50 chars'})
    password = forms.CharField(min_length=4, required=True,
                               widget=forms.PasswordInput,
        error_messages={'required': 'Password needed',
                       'min_length': '4 chars or more please'})

    def clean(self):
        cleaned_data = self.cleaned_data
        user = authenticate(username=cleaned_data.get("name"), password=cleaned_data.get("password"))
        if user is None or not user.is_active:
            if user is None :
                msg = 'Identification incorrecte.'
            elif not user.is_active:
                msg = 'Vous êtes désactivé.'
            self._errors["name"] = self.error_class([msg])
#            del cleaned_data["name"]
#            del cleaned_data["password"]
        return cleaned_data

class ProfileForm(ModelForm):
    first_name = forms.CharField(min_length=2, max_length=50, required=False, initial="prenom",
        error_messages={'min_length': 'Minimal length : 2 chars',
                        'max_length': 'Maximal length : 50 chars',})
    last_name = forms.CharField(min_length=2, max_length=100, required=False,
        error_messages={'min_length': 'Minimal length : 2 chars',
                        'max_length': 'Maximal length : 100 chars'})
    phone = forms.RegexField(regex='^0[1-9]([-. ]?[0-9]{2}){4}$', required=False,
        error_messages={'invalid': 'Format incorrect'})
    place = forms.CharField(max_length=300, required=False,
        error_messages={'max_length': 'Taille maximale : 300 caractères'})
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone', 'place')

