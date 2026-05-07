from django.shortcuts import render, redirect
from .models import Licenciatura, Docente, UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, MakingOf
from .forms import ProjetoForm

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

# LISTA DE PROJETOS
def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'app/projetos.html', {'projetos': projetos})    

# FORM para adicionar projeto

def projeto_novo_view(request):

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projetos')

    else:
        form = ProjetoForm()

    return render(request, 'app/projeto_novo.html', {
        'form': form
    })