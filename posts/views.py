from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def home(request): 
    majors = Major.objects.all()
    return render(request,'posts/home.html' , {'majors':majors}) 


def major_courses(request , id):
    courses = Course.objects.filter(major = id)
    return render (request , 'posts/major_courses.html' , {'courses' : courses}) 



def my_courses (request):

    student = Student.objects.get(uni_number=request.user.username)
    major = Major.objects.get(name= student.major)
    courses = Course.objects.filter(major = major.id) 
    return render (request , 'posts/major_courses.html' , {'courses' : courses})


def search (request) :
    course = None
    if request.method == 'GET' :
        dic = request.GET # dictionary of keys and values of form key is the name 
        name = dic.get("q") 
        
        if name is not None :
          course = get_object_or_404(Course,name=name)
          

    return render(request , 'posts/search.html' , {'course': course})

    


def course_detail(request , id):
        
    mes = ""
    course = Course.objects.get(id=id)
    current_student = Student.objects.get(uni_number = request.user.username)


    if request.method == 'POST' :
        
        obj = StudentCourse.objects.filter(student= current_student , course=course)

        if request.POST.get("add"):
            if not obj.exists():
                assign = StudentCourse.objects.create(course=course , student = current_student)
                mes = "Course added"
            else:
                mes = "You already added this course !"

        elif request.POST.get("delete"):
            if obj.exists():
                obj.delete()
                mes ="Course is deleted" 
            else:
                mes = "You can't delete unregistered course"

    return render (request , 'posts/search.html', {'course': course , 'current': current_student ,'mes':mes})
