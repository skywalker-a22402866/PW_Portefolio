from django.shortcuts import render, redirect, get_object_or_404
from .models import Licenciatura, Docente, UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, MakingOf
from .forms import ProjetoForm
import markdown
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def is_gestor(user):
    return user.groups.filter(name='gestor-portfolio').exists()

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

# LISTA de UNIDADES
def unidades_view(request):
    unidades = UnidadeCurricular.objects.all()
    return render(request, 'app/unidades.html', {'unidades': unidades})       

# LISTA de COMPETENCIAS
def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'app/competencias.html', {'competencias': competencias}) 

# LISTA de COMPETENCIAS
def makingOfs_view(request):
    makingOfs = MakingOf.objects.all()
    return render(request, 'app/makingOf.html', {'makingOfs': makingOfs})      


# FORM para adicionar projeto
@login_required
@user_passes_test(is_gestor)
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

#FORM edição Projeto
def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)

    #print(form)  # vê no terminal
    return render(request, 'app/editar_projeto.html', {'form': form})

#Apagar Projeto
def apagar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')

    return render(request, 'app/apagar_projeto.html', {'projeto': projeto})

#Pagina sobre
def sobre_view(request):
    texto_md = """

# TITULO

## Sub-Titulo

Esta frase é de exempo.

* item 1
* item 2
* item 3

"""
    texto_html = markdown.markdown(texto_md)
    return render (request, 'app/sobre.html', {'texto':texto_html})
