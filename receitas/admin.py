from django.contrib import admin
from .models import Receitas
# Register your models here.

class DisplayReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita')
    list_display_links = ('id', 'nome_receita')

admin.site.register(Receitas, DisplayReceitas)