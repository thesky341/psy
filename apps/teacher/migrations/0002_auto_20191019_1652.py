# Generated by Django 2.2.5 on 2019-10-19 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentClass', verbose_name='教师上课班级'),
        ),
    ]
