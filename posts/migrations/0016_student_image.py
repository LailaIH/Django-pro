# Generated by Django 4.1.1 on 2022-10-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_studentcourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='B.png', upload_to='profile_pics'),
        ),
    ]