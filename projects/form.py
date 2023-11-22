import django_tables2 as tables
from projects.models import *

class SimpleTable(tables.Table):

    title_project = tables.Column(verbose_name='Наименование инвестиционного проекта или мероприятия')
    otvProject = tables.Column(verbose_name='Уровень и ответственный исполнитель')
    plan_work = tables.Column(verbose_name='Объем освоения, млн. руб. (без НДС) ПЛАН')
    fact_work = tables.Column(verbose_name='Объем освоения, млн. руб. (без НДС) ФАКТ')
    number_row = tables.Column(verbose_name='№ п/п')
    plan_stage_work = tables.Column(verbose_name='Этап работы или контрольные точки на отчетный год ПЛАН')
    fact_stage_work = tables.Column(verbose_name='Этап работы или контрольные точки на отчетный год ФАКТ')
    plan_work_gov = tables.Column(verbose_name='в том числе из средств федерального бюджета, млн. руб. ПЛАН')
    fact_work_gov = tables.Column(verbose_name='в том числе из средств федерального бюджета, млн. руб. ФАКТ')
    reason = tables.Column(verbose_name='Причина невыполнения')

    class Meta:
        model = Projects
        attrs = {'class': 'table table-bordered table-hover',
                 'th': {'class': 'table-blue middle', 'style': 'text-align: center'}
                 }
        models.OneToOneField(FinancialProject2023, on_delete=models.PROTECT)
        fields = ['number_row', 'otvProject', 'title_project', 'plan_stage_work',
                  'fact_stage_work', 'plan_work', 'fact_work',
                  'plan_work_gov', 'fact_work_gov', 'reason'
                  ]
        template_name = "django_tables2/bootstrap5-responsive.html"
        orderable = False


