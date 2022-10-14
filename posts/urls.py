from django.urls import path , include
from . import views

app_name ='posts'

urlpatterns = [
    path('', views.home , name='home'), 
    path('<int:id>', views.major_courses , name='major_courses'),
    path('my_courses', views.my_courses , name='my_courses'),
    path('search', views.search , name='search'), 
     path('course_detail/<int:id>', views.course_detail , name='course_detail'), 
    
]