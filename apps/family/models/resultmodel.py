from django.db import models
from .familymodel import FamilyBasic
from .classmodel import FamilyClass
from django.utils.html import format_html
class Result(models.Model):
    class Meta:
        verbose_name = '家庭考核成绩'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(FamilyClass, on_delete=models.CASCADE, verbose_name='班级',null=True,blank=True)
    relate_family = models.OneToOneField(FamilyBasic, on_delete=models.CASCADE, verbose_name='学号', blank=True, null=True)
    homework_one_result = models.CharField(max_length=128,verbose_name='作业一成绩',null=True,blank=True,default='空')
    date = models.CharField(max_length=128,verbose_name='考核日期',blank=True,null=True,default='空')
    homework_two_result = models.CharField(max_length=128,verbose_name='作业二成绩',blank=True,null=True,default='空')
    homework_three_result = models.CharField(max_length=128,verbose_name='作业三成绩',blank=True,null=True,default='空')
    result = models.CharField(max_length=64,verbose_name='合格情况',choices=(('合格','合格'),('不合格','不合格')),blank=True,null=True,default='空')
    total = models.CharField(max_length=128,verbose_name='总分',null=True,blank=True,default='空')
    nation_result = models.CharField(max_length=128,verbose_name='国考笔试成绩',null=True,blank=True,default='空')
    pre = models.CharField(max_length=128,verbose_name='说课分',null=True,blank=True,default='空')
    speech = models.CharField(max_length=128,verbose_name='宣讲分',null=True,blank=True,default='空')
    other = models.CharField(max_length=128,verbose_name='备注',null=True,blank=True,default='空')

    def get_fam_name(self):
        info = self.relate_family.fam_name
        if self.relate_family.familytuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_fam_name.short_description = u'姓名'
    get_fam_name.allow_tags = get_fam_name.is_column = True

    get_fam_name.short_description = u'姓名'
    get_fam_name.allow_tags = get_fam_name.is_column = True

    def get_fam_num(self):
        return self.relate_family.fam_number

    get_fam_num.short_description = '学号'
    get_fam_num.allow_tags = get_fam_num.is_colume = True

    def get_fam_class(self):
        return self.relate_family.fam_class.class_name

    get_fam_class.short_description = u'班级'
    get_fam_class.allow_tags = get_fam_name.is_column = True

    def __str__(self):
        return str(self.relate_family.fam_name)