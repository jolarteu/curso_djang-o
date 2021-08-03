

# Django
from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):

    username = forms.CharField(label='',min_length=4, max_length=50,
    widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'required': True
                }))
    password= forms.CharField(label='',max_length=15, widget=forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'required': True
            }
        ))
    password_confirmation = forms.CharField(label='',max_length=15, widget=forms.PasswordInput(attrs={
                'placeholder': 'password confirmation',
                'class': 'form-control',
                'required': True
            }
        ))

    first_name= forms.CharField(label='',min_length=2, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder':'First name',
                'class': 'form-control',
                'required': True
                }
            ))
    last_name= forms.CharField(label='',min_length=2, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last name',
                'class': 'form-control',
                'required': True
                }
        ))

    email = forms.CharField(label='',min_length=5, max_length=50, widget=forms.EmailInput(
        attrs={
                    "placeholder": "email",
                    "class": "form-control",
                    'required': True
                }
        ))

    def clean_username(self):

        username=self.cleaned_data['username']
        username_taken= User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('username is already in use')
        return username

    def  clean(self):

        data= super().clean()

        password= data['password']
        password_confirmation= data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError(r"password don't match")

        return data

    def save(self):
            data = self.cleaned_data
            data.pop('password_confirmation')

            user = User.objects.create_user(**data)
            profile = Profile(user=user)
            profile.save()


class ProfileForm(forms.Form):
    picture = forms.ImageField()
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
