from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import Labour_data

class signupform(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Repeat Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','first_name','email')
        label={'first_name':'Name'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 
                 'email':forms.EmailInput(attrs={'class':'form-control'}),}
        
class loginform(AuthenticationForm):
    class Meta:
        username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control','display':'block'}))
        password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','display':'block'})) 
        
class labourform(forms.ModelForm):
    class Meta:
        model=Labour_data
        exclude=('user',)
        labels={'no_of_w':'No of Workers','other_type':'other type'}
        widgets={
            'type':forms.Select(attrs={'class':'form-control'}),
            'other_type':forms.TextInput(attrs={'class':'form-control','placeholder':'if your work type not present'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'full name'}),
            'location':forms.TextInput(attrs={'class':'form-control','placeholder':'Try to give full address....'}),
            'salary':forms.NumberInput(attrs={'class':'form-control','placeholder':'salary for one worker...'}),
            'no_of_w':forms.NumberInput(attrs={'class':'form-control','placeholder':'mention how much labours with you currently..'}),
            'contact':forms.NumberInput(attrs={'class':'form-control'}),
            'other_details':forms.TextInput(attrs={'class':'form-control py-5',}),
        }
        
        