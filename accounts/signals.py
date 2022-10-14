from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from posts.models import Student , Profile 


@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
       
       Student.objects.create(uni_number=instance.username , first_name="student")



@receiver(post_save, sender=Student)
def create_profile(sender, instance, created, **kwargs):
    if created:
       
       Profile.objects.create(student = instance)


