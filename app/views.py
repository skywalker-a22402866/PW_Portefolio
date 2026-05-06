from django.shortcuts import render
from .models import Licenciatura, Docente, UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, MakingOf

# Create your views here.
def index_view(request):
    return render(request, 'app/index.html')

# LISTA DE LICENCIATURAS
def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'app/licenciaturas.html', {'licenciaturas': licenciaturas})

# LISTA DE TFCS
def tfcs_view(request):
    TFCs = TFC.objects.all()
    return render(request, 'app/tfcs.html', {'tfcs': TFCs})

# LISTA DE DOCENTES
def docentes_view(request):
    docentes = Docente.objects.all()
    return render(request, 'app/docentes.html', {'docentes': docentes})