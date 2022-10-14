# Generated by Django 4.1.1 on 2022-10-06 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_rename_firstt_name_student_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.major'),
        ),
    ]