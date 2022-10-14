from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from posts.models import Student , Profile 


class UserForm(UserCreationForm):
    
    class Meta :
        model = User
        fields = ['username','password1','password2']


class StudentEditForm(forms.ModelForm):
    class Meta :
        model = Student
        fields = ['first_name' , 'last_name' , 'major' , 'image']


class ProfileEditForm(forms.ModelForm):
    class Meta :
        model = Profile
        fields = ['phone_number']        


