from django.shortcuts import render, redirect, get_object_or_404
from .models import Licenciatura, Docente, UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, MakingOf, Artigo, Comentario
from .forms import ProjetoForm, ArtigoForm, ComentarioForm
import markdown
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group



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
#@user_passes_test(is_staff)
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
@login_required
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
@login_required
def apagar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')

    return render(request, 'app/apagar_projeto.html', {'projeto': projeto})

#Pagina artigos
def artigos_view(request):
    artigos = Artigo.objects.all()
    return render(request, 'app/artigos.html', {'artigos': artigos})      

# FORM para adicionar projeto
@login_required
#@user_passes_test(is_staff)
def artigo_novo_view(request):

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('artigos')

    else:
        form = ArtigoForm()

    return render(request, 'app/artigo_novo.html', {
        'form': form
    })

def comentario_novo_view(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.save()

            return redirect('artigos')

    else:
        form = ComentarioForm()

    return render(
        request,
        'app/comentario_novo.html',
        {
            'form': form,
            'artigo': artigo
        }
    )



#Pagina sobre
def sobre_view(request):
    texto_md = """

# UM POUCO SOBRE MIM...

## Nuno Tainha

Aluno de LEI e já com curso de Engenharia Electrotecnia.

* Forte aptidões para Sistemas Digitais
* Gosto de trabalho de redes
* Vejo me mais como programador de hardware, área que mais aprecio.


"""
    texto_html = markdown.markdown(texto_md)
    return render (request, 'app/sobre.html', {'texto':texto_html})



def registo_view(request):
    if request.method == "POST":
        username = request.POST["username"]

        if User.objects.filter(username=username).exists():
            return render(request, "app/registo.html", {
                "erro": "Esse username já existe."
            })

        user = User.objects.create_user(
            username=username,
            email=request.POST["email"],
            first_name=request.POST["nome"],
            last_name=request.POST["apelido"],
            password=request.POST["password"]
        )

        grupo, _ = Group.objects.get_or_create(name="bloggers")
        user.groups.add(grupo)

        return redirect("login")

    return render(request, "app/registo.html")


def like_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    artigo.likes += 1
    artigo.save()

    return redirect('artigos')

def videotutoriais_view(request):
    return render(request, 'app/videotutoriais.html')