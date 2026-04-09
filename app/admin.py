from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Utilizador)

# Registar modelos simples
admin.site.register(Licenciatura)
admin.site.register(Docente)
admin.site.register(Tecnologia)
admin.site.register(Formacao)
admin.site.register(MakingOf)
admin.site.register(TFC)
