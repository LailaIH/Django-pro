# Generated by Django 4.1.1 on 2022-10-02 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_student_first_name_student_firstt_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='firstt_name',
            new_name='first_name',
        ),
    ]