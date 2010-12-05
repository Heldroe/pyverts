# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import Profile
from cars.models import Car
from itineraries.models import Itinerary

class SignupForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50, required=True, label='Pseudo',
        error_messages={'required': 'Name is missing',
                        'min_length': 'Minimal length : 2 chars',
                        'max_length': 'Maximal length : 50 chars'})
    password = forms.CharField(min_length=4, required=True,label='Mot de passe',
                               widget=forms.PasswordInput,
        error_messages={'required': 'Password needed',
                       'min_length': '4 chars or more please'})
    password2 = forms.CharField(min_length=4, required=True,label='Répétez le mot de passe',
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
    name = forms.CharField(min_length=2, max_length=50, required=True,label='Pseudo',
        error_messages={'required': 'Name is missing',
                        'min_length': 'Minimal length : 2 chars',
                        'max_length': 'Maximal length : 50 chars'})
    password = forms.CharField(min_length=4, required=True,label='Mot de passe',
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
    first_name = forms.CharField(min_length=2, max_length=50, required=False, label='Prénom',
        error_messages={'min_length': 'Minimal length : 2 chars',
                        'max_length': 'Maximal length : 50 chars',})
    last_name = forms.CharField(min_length=2, max_length=100, required=False, label='Nom de famille',
        error_messages={'min_length': 'Minimal length : 2 chars',
                        'max_length': 'Maximal length : 100 chars'})
    phone = forms.RegexField(regex='^0[1-9]([-. ]?[0-9]{2}){4}$', required=False,label='Numéro de téléphone',
        error_messages={'invalid': 'Format incorrect'})
    place = forms.CharField(max_length=300, required=False, label='Votre emplacement',
        error_messages={'max_length': 'Taille maximale : 300 caractères'})
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone', 'place')

class NewCarForm(ModelForm):
    model = forms.CharField(min_length=2, max_length=100, required=True,
        error_messages={'min_length': 'Le nom du modèle doit faire au moins 2 caractères.',
                        'max_length': 'Le nom du modèle ne peut pas dépasser 100 caractères.',
                        'required': 'Vous devez définir un modèle.'})
    seats = forms.IntegerField(min_value=2, max_value=20, required=True,
        error_messages={'min_value': 'Le nombre de places minimal est 2.',
                        'max_value': 'Le nombre de places maximal est 20.',
                        'invalid': 'Le nombre de places doit être entier.',
                        'required': 'Vous devez définir un nombre de places.'})
    consumption = forms.DecimalField(min_value=2, max_value=50, required=True,
                                     max_digits=5,
        error_messages={'max_digits': 'La précision de la consommation ne doit pas dépasser 5 chiffres',
                        'max_value': 'La consommation maximale ne doit pas dépasser 50L/100km',
                        'min_value': 'La consommation minimale est de 2L/100km',
                        'required': 'Vous devez définir une consommation en litres par 100km'})

    fuel_type = forms.ChoiceField(choices=settings.ESSENCE_TYPES,required=True,
        error_messages={'required': 'Vous devez choisir un type d\'essence',
                        'invalid_choice': 'Vous devez choisir un élément de la liste'})
    class Meta:
        model = Car
        fields = ('model', 'seats', 'consumption', 'fuel_type', 'accessibility')

class NewItineraryForm(ModelForm):
    depart = forms.CharField(required=True, min_length=2, max_length=200,label='Lieu de départ',
        error_messages={'required': 'Vous devez définir un lieu de départ',
                        'min_length': 'Le lieu doit faire au moins 2 caractères',
                        'max_length': 'Le lieu doit faire au maximum 200 caractères'})
    arrival = forms.CharField(required=True, min_length=2, max_length=200,label='Lieu d\'arrivée',
        error_messages={'required': 'Vous devez définir un lieu d\'arrivée',
                        'min_length': 'Le lieu doit faire au moins 2 caractères',
                        'max_length': 'Le lieu doit faire au maximum 200 caractères'})
    depart_hour = forms.CharField(required=True, min_length=10, max_length=100,label='Heure de départ',
        error_messages={'required': 'Vous devez définir une date de départ',
                        'min_length': 'La date doit faire au moins 10 caractères',
                        'max_length': 'La date ne doit pas dépasser 100 caractères'})

    class Meta:
        model = Itinerary
        fields = ('depart', 'arrival', 'depart_hour', 'reserved_seats', 'itinerary_cost')
