from django import forms
from .models import User
class Student(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name','email','password')
        labels = {'name':'Enter your Name','email':'Enter your Email','password':'Enter your Password'}
        widgets = {'password':forms.PasswordInput,
                   'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Name here'}),
                   'email':forms.TextInput(attrs={'class':'myclass','placeholder':'Email here'}),
                   'password':forms.TextInput(attrs={'class':'myclass','placeholder':'Password here'})}
        error_messages = {'name':{'required':'Enter your name please'},
                          'email':{'required':'Enter your email please'},
                          'password':{'required':'Enter your password please'}}
        
