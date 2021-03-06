from django.contrib import admin

from pessoas.models import Pessoa

class DisplayPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10


admin.site.register(Pessoa, DisplayPessoas)