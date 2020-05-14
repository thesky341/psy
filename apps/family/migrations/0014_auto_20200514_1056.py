# Generated by Django 2.2.5 on 2020-05-14 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0013_auto_20200510_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='familybasic',
            name='fam_group',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='组名与职务'),
        ),
        migrations.AddField(
            model_name='familybasic',
            name='fam_type',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='学员类型'),
        ),
        migrations.AddField(
            model_name='familycertification',
            name='cert_nation_id',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='国证证书编号'),
        ),
        migrations.AddField(
            model_name='familycertification',
            name='cert_nation_people',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='国证证书领取人与日期'),
        ),
        migrations.AddField(
            model_name='familycertification',
            name='cert_other',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='familytextbook',
            name='text_basic2',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='教材2'),
        ),
        migrations.AddField(
            model_name='familytextbook',
            name='text_guide',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='培训指南'),
        ),
        migrations.AddField(
            model_name='familytuition',
            name='fee_exam',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='考试费'),
        ),
        migrations.AddField(
            model_name='familytuition',
            name='fee_exam_extra',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='补考费'),
        ),
        migrations.AddField(
            model_name='familytuition',
            name='fee_info',
            field=models.TextField(blank=True, default='空', max_length=128, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='familytuition',
            name='fee_invoice_inc',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='出票单位'),
        ),
        migrations.AddField(
            model_name='familytuition',
            name='fee_material',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='资料费'),
        ),
        migrations.AddField(
            model_name='familytuition',
            name='fee_total',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='总费用'),
        ),
        migrations.AddField(
            model_name='familywechat',
            name='wechat_other',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='result',
            name='nation_result',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='国考笔试成绩'),
        ),
        migrations.AddField(
            model_name='result',
            name='other',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='result',
            name='pre',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='说课分'),
        ),
        migrations.AddField(
            model_name='result',
            name='speech',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='宣讲分'),
        ),
        migrations.AddField(
            model_name='result',
            name='total',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='总分'),
        ),
        migrations.AlterField(
            model_name='familytextbook',
            name='text_basic',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='教材1'),
        ),
    ]