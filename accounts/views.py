from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth import authenticate , login
from posts.models import Student , Profile
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 



def signup(request):
    if request.method == 'POST' :

        form = UserForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            

            user = authenticate(username=username,password=password)
            login(request , user)


    else :
        form = UserForm() 


    return render(request , 'registration/signup.html' , {'form':form})


@login_required
def profile(request):

    current_student = Student.objects.get(uni_number = request.user.username)
    

    student = Student.objects.get(uni_number = request.user.username)
    profile = Profile.objects.get(student= student)

    if request.method == 'POST' :
        sform = StudentEditForm(request.POST ,request.FILES , instance=student )
        pform = ProfileEditForm(request.POST , instance=profile)

        if sform.is_valid() and pform.is_valid():
            sform.save()
            pform.save()
            messages.success(request , f'Profile updated successfully!' )
            return redirect(reverse('accounts:profile'))




    else :
      sform =  StudentEditForm(instance = student)
      pform =  ProfileEditForm(instance = profile)   




    return render (request , 'accounts/profile.html' , {'sform' : sform , 'pform': pform})