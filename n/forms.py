from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from n.models import *
from django.contrib.auth.forms import UserCreationForm




class User_infoForm(ModelForm):
    class Meta:
        model = user_profile
        fields = ['childhood_and_Education', 'childhood_and_Education_Photo', 'About_Me','About_Me_Photo' ,'Personal_Life', 'Personal_Life_Photo', 'Political_Career','Political_Career_Photo','aims_Goal_and_Dream', 'aims_Goal_and_Dream_Photo','Message_For_Followers', 'Photo']
                 
    #    exclude = ('user',)

class PasswordForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (Again)', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username',  'email']
        labels = {'email': 'Email'}


# Create your forms here.



    