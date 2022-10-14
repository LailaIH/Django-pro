from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Major(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    name = models.CharField(max_length=25)



    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.CharField(max_length=25)
    number = models.CharField(max_length=25)
    lecturer= models.ForeignKey(Lecturer , on_delete=models.CASCADE)
    major= models.ForeignKey(Major , on_delete=models.CASCADE)


    def __str__(self):
        return self.name




class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    uni_number = models.CharField(max_length=9, validators=[MinLengthValidator(9)] , default='')
    major = models.ForeignKey(Major , on_delete=models.CASCADE , default=1)
    image = models.ImageField(default='B.png', upload_to="profile_pics")
    
    

    def __str__(self):
        return self.first_name 



class Profile(models.Model):
    student = models.OneToOneField(Student , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11) 

    def __str__(self):
        return str(self.student) 



class StudentCourse(models.Model)  :
    student = models.ForeignKey(Student,on_delete= models.CASCADE , null=True, blank=True)
    course = models.ForeignKey(Course,on_delete= models.CASCADE , null=True, blank=True)  
     


