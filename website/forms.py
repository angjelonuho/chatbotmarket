from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class SignUpForm(UserCreationForm):

    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control','name': 'Your name'}))
    password1 = forms.CharField(label="Card Number" ,widget= forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control'}))
  

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

        # labels = {
        #  'username': _('Username'),
        #  'email': _('E-mail Address'),
        #  'password1' : _('Password'), 
        #  'password2' : _('Confirm Password'),
        # }

        widgets = {
          'username': forms.TextInput(attrs={'class':'form-control'}),

        }
    
    def save(self,commit=True):
    	user = super(SignUpForm , self).save(commit=False)
    	user.email = self.cleaned_data['email']

    	if commit:
    		user.save()

    	return user