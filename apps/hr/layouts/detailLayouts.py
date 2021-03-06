from django.utils.translation import ugettext as _
from xadmin.layout import Fieldset, Main, Side, Row
StaffLayout = \
    (
        Main(
            Fieldset(_('职工状态'),
                     'at_post',
                     ),
            Fieldset(_('个人信息'),
                     'personal_name',
                     'personal_gender',
                     'personal_id_num',
                     'personal_birth_date',
                     'personal_soc_ins',
                     'personal_soc_ins_id',
                     Row('personal_folk', 'personal_reg_location'),
                     'personal_current_location',
                     'personal_is_marry',
                     'personal_status',
                     Row('personal_phone', 'personal_phone_other'),
                     Row('personal_emer_phone', 'personal_emer_people'),
                     ),
            Fieldset(_('工作信息'),
                     Row('work_enter_date', 'work_dismiss_date'),
                     'work_hire_method',
                     'personal_on_market',
                     'work_department',
                     'work_duty',
                     'work_duty_hire_date',
                     ),
            Fieldset(_('职称信息'),
                     'work_title',
                     'work_set_rank_date',
                     'work_hire_rank_aca_date',
                     'work_position'
                     ),
            Fieldset(_('教育信息'),
                     'edu_background',
                     'edu_grade',
                     'edu_learn_exp',
                     ),
        ),
        Side(
            Fieldset('其他信息',
                     'other_avatar',
                     'other_more')
        ),
    )