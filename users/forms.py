from django import forms
from django.core import validators
from users.models import User
from django.contrib.auth import authenticate


class SignUpValidation(forms.ModelForm):
    """
    sign up validation
    """
    confirm = forms.CharField()
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password',)

    def clean_email(self):
        email = User.objects.filter(email=self.cleaned_data['email'])
        if email.exists():
            raise forms.ValidationError('Email already exists!')
        return self.cleaned_data['email']

    def clean(self):
        confirm = self.cleaned_data.get('confirm')
        password = self.cleaned_data.get('password')

        if confirm != password:
            raise forms.ValidationError('Passwords do not match!')
        return self.cleaned_data


class LoginValidation(forms.ModelForm):
    """
    login validation
    """
    email = forms.EmailField()

    
    class Meta:
        model = User
        fields = ('email', 'password',)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(username=email,password=password)

        if user is not None:
            return self.cleaned_data
        raise forms.ValidationError('Incorrect email or password')


