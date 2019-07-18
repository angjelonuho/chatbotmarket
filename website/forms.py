from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class SignUpForm(UserCreationForm):

    email = forms.EmailField(label = "Email" , widget= forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label = "Password" ,widget= forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = "Confirm Password" ,widget= forms.PasswordInput(attrs={'class':'form-control'} , ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )


        widgets = {
          'username': forms.TextInput(attrs={'class':'form-control'}),

        }
    
    def save(self,commit=True):
    	user = super(SignUpForm , self).save(commit=False)
    	user.email = self.cleaned_data['email']

    	if commit:
    		user.save()

    	return user