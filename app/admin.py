from django.contrib import admin

# Register your models here.
from app.models import Utilizador
admin.site.register(Utilizador)

from django.contrib import admin
from .models import (
    Licenciatura, UnidadeCurricular, ImagemUC, Projeto,
    Docente, TFC, Tecnologia, Formacao, Competencia, MakingOf
)

# Registar modelos simples
admin.site.register(Licenciatura)
admin.site.register(Docente)
admin.site.register(Tecnologia)
admin.site.register(Formacao)
admin.site.register(MakingOf)

# Registar modelos com inlines (opcional mas recomendado)
class ProjetoInline(admin.TabularInline):
    model = Projeto
    extra = 1

class ImagemUCInline(admin.TabularInline):
    model = ImagemUC
    extra = 1

class UnidadeCurricularAdmin(admin.ModelAdmin):
    inlines = [ProjetoInline, ImagemUCInline]
    list_display = ('nome', 'licenciatura', 'semestre', 'ects')
    list_filter = ('licenciatura', 'semestre')
    search_fields = ('nome',)

admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)

class TFCAdmin(admin.ModelAdmin):
    list_display = ('nome', 'docente')
    filter_horizontal = ('tecnologias',)

admin.site.register(TFC, TFCAdmin)
