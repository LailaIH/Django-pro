# Generated by Django 4.1.1 on 2022-10-06 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.student')),
            ],
        ),
    ]