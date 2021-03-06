# Generated by Django 2.2.5 on 2019-10-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbasic',
            name='stu_gender',
            field=models.CharField(blank=True, choices=[('男', '男'), ('女', '女')], max_length=16, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='studentbasic',
            name='stu_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='studenttextbook',
            name='text_other',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
    ]
