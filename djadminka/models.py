from django.db import models


class Vacanci(models.Model):
    Title = models.TextField(
        verbose_name='Название',
    )
    Link = models.URLField(
        'Ссылка на вакансию'
    )
    Salary = models.TextField(
        'Зарплата'
    )
    No_resume = models.BooleanField(
        'Можно ли откликаться без резюме'
    )
    First = models.BooleanField(
        'Будете ли вы первым, откликаясь на эту вакансию'
    )
    Company = models.TextField(
        'Компания'
    )
    Date = models.TextField(
        'Дата публикации вакансии'
    )
    Address = models.TextField(
        'Адрес'
    )

    class Meta:
        verbose_name = "Вакансии"
        verbose_name_plural = "Вакансии"


class Vacanci_2(models.Model):
    Title = models.TextField(
        verbose_name='Название',
    )
    Link = models.URLField(
        'Ссылка на вакансию'
    )
    Price = models.TextField(
        'Зарплата'
    )
    Number_of_otkliks = models.TextField(
        'Количество откликов'
    )
    Number_of_vues = models.TextField(
        'Количество просмотров другими пользователями'
    )

    class Meta:
        verbose_name = "Вакансии_2"
        verbose_name_plural = "Вакансии_2"
