# Generated by Django 2.2.5 on 2019-10-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20191021_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onduty',
            options={'verbose_name': '考勤信息', 'verbose_name_plural': '考勤信息'},
        ),
        migrations.AlterModelOptions(
            name='studentbasic',
            options={'verbose_name': '招生信息', 'verbose_name_plural': '招生信息'},
        ),
        migrations.RemoveField(
            model_name='studentbasic',
            name='stu_profession',
        ),
        migrations.AddField(
            model_name='studentbasic',
            name='stu_level',
            field=models.CharField(blank=True, choices=[('二级', '二级'), ('三级', '三级')], max_length=16, null=True),
        ),
    ]
