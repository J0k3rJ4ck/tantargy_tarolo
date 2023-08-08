from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Tantargy
from django.contrib import messages
from accounts.models import  Kovetelmeny



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class TantargyForm(forms.ModelForm):
    class Meta:
        model = Tantargy
        fields = ('nev',)




class KovetelmenyForm(forms.ModelForm):
    class Meta:
        model = Kovetelmeny
        fields = '__all__'
        exclude = ['felhasznalo']  # csak a felhasznalo mezőt zárjuk ki

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(KovetelmenyForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['tantargy'].queryset = Tantargy.objects.filter(felhasznalo=user)
