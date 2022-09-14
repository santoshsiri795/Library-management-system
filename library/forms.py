from django.core import validators
from django import forms
from .models import Library
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField



class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields =['Book_name','Author_name','description']
        widgets ={
            'Book_name':forms.TextInput(attrs={'class':'form-control'}),
            'Author_name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),

        }


class SignUpForm(UserCreationForm):
    password1= forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='confirm password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        #labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets= {'username':forms.TextInput(attrs={'class':'form-control'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.EmailInput(attrs={'class':'form-control'}),

        }

class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password= forms.CharField(label=("password"), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

