from django.db import models
from djmoney.models.fields import MoneyField
from datetime import date

# Create your models here.

# Инновационные технологии список
TECHNOLOGY = (
    ('Раздел 1', 'Интелектуальные ПС'),
    ('Раздел 2', 'Активно-адаптивные сети'),
    ('Раздел 3', 'Бизнес процессы'),
    ('Раздел 4', 'Новые технологии'),
    ('Раздел 5', 'НИОКР'),
    ('Раздел 6', 'Система управления'),
    ('Раздел 7', 'Кадровый потенциал'),
)

# Наименование компании ДО списком
NAME_COMP = (
    ('РЮ', 'Россети Юг'),
)

class Projects(models.Model):

    # Наименование инвестиционного проекта
    title_project = models.TextField(unique=True, primary_key=True)
    # Наименование компании
    title_comp = models.CharField(choices=NAME_COMP, max_length=32)
    # Инновационные технологии
    tech_project = models.CharField(choices=TECHNOLOGY, max_length=32)
    # Начало реализации проекта
    date_start = models.DateField()
    # Окончание реализации проекта
    date_finish = models.DateField()
    # Результаты планируемые к получению по проекту
    result = models.TextField(null=True, blank=True)
    # Уровень и ответственный исполнитель
    otvProject = models.TextField(null=True, blank=True)
    # Идентификатор инвестиционного проекта
    id_inv_pr = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_project

class FinancialProject2023(models.Model):

    # Наименование инвестиционного проекта
    title_project = models.ForeignKey(to=Projects, on_delete=models.PROTECT)

    # План рассмотренный руководителем проекта и согласованный
    plan_consider = MoneyField(
            decimal_places=2,
            default_currency='RUB',
            max_digits=5,
            default=0,
            )

    # План корректируемый ДО
    plan_work = MoneyField(
            decimal_places=2,
            default_currency='RUB',
            max_digits=5,
            default=0,
            )

    # Факт рассмотренный руководителем проекта и согласованный
    fact_consider = MoneyField(
            decimal_places=2,
            default_currency='RUB',
            max_digits=5,
            default=0,
            )

    # Факт корректируемый ДО
    fact_work = MoneyField(
            decimal_places=2,
            default_currency='RUB',
            max_digits=5,
            default=0,
            )

    # Плановый этап работы:
    plan_stage_work = models.TextField(null=True, blank=True)
    plan_stage_consider = models.TextField(null=True, blank=True)

    # Фактический этап работы:
    fact_stage_work = models.TextField(null=True, blank=True)
    fact_stage_consider = models.TextField(null=True, blank=True)

    # Порядковый номер:
    number_row = models.TextField(null=True, blank=True)

    # Причина не выполнения
    reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_project

class FinancialCompany2023(models.Model):

    # Наименование компании
    title_comp = models.ForeignKey(to=Projects, on_delete=models.PROTECT)
    # Собственная выручка
    own_revenue = MoneyField(
        decimal_places=2,
        default_currency='RUB',
        max_digits=10,
        default=0,
    )
    # Объем инвестиционной программы
    vol_invest = MoneyField(
        decimal_places=2,
        default_currency='RUB',
        max_digits=10,
        default=0,
    )

    def __str__(self):
        return self.title_comp

class FinancialProjectGov2023(models.Model):

    # Наименование инвестиционного проекта
    title_project = models.ForeignKey(to=Projects, on_delete=models.PROTECT)

    # План рассмотренный руководителем проекта и согласованный
    plan_consider_gov = MoneyField(
        decimal_places=2,
        default_currency='RUB',
        max_digits=5,
        default=0,
    )

    # План корректируемый ДО
    plan_work_gov = MoneyField(
        decimal_places=2,
        default_currency='RUB',
        max_digits=5,
        default=0,
    )

    # Факт рассмотренный руководителем проекта и согласованный
    fact_consider_gov = MoneyField(
        decimal_places=2,
        default_currency='RUB',
        max_digits=5,
        default=0,
    )

    # Факт корректируемый ДО
    fact_work_gov = MoneyField(
        decimal_places=2,
        default_currency='RUB',
        max_digits=5,
        default=0,
    )

    def __str__(self):
        return self.title_project
