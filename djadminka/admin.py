from django.contrib import admin
from .models import Vacanci, Vacanci_2
from .forms import Vacanci_Forms, Vacanci_Forms_2


@admin.register(Vacanci)
class Vacanci_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Link', 'Salary', 'No_resume', 'First', 'Company', 'Date', 'Address')
    form = Vacanci_Forms

@admin.register(Vacanci_2)
class Vacanci_Admin(admin.ModelAdmin):
    list_display = ('Title', 'Link', 'Price', 'Number_of_otkliks', 'Number_of_vues')
    form = Vacanci_Forms_2