from.models import*
from django import forms
from django.contrib.auth.forms import UserCreationForm


class utilisateurForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    ),
    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    ),
    
    class Meta (UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields + ('password1','password2')

class tacheForm(forms.ModelForm):
    class Meta:
        model= Tache
        fields= '__all__'