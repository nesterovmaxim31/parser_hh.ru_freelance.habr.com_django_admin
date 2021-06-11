# Generated by Django 3.0.2 on 2021-06-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacanci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(verbose_name='Название')),
                ('Link', models.URLField(verbose_name='Ссылка на вакансию')),
                ('Salary', models.TextField(verbose_name='Зарплата')),
                ('No_resume', models.BooleanField(verbose_name='Можно ли откликаться без резюме')),
                ('First', models.BooleanField(verbose_name='Будете ли вы первым, откликаясь на эту вакансию')),
                ('Company', models.TextField(verbose_name='Компания')),
                ('Date', models.TextField(verbose_name='Дата публикации вакансии')),
                ('Address', models.TextField(verbose_name='Адрес')),
            ],
        ),
    ]
