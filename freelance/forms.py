from django.contrib.auth.models import User
from django import forms
from .models import Jobs,Projects

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}))
    class Meta:
        model = User
        fields =  ['username',
                   'email','first_name','last_name','password']

class PostJobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['title','domain','job_desc']

class PostProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title','domain','project_desc']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username' , 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Password', 'class':'form-control'}))
    fields = ['username','password']
