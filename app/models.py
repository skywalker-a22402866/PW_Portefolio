from django.db import models

# Create your models here.

# ======================
# Licenciatura
# ======================
class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='app/licenciaturas/', blank=True, null=True)

    def __str__(self):
        return self.nome

# ======================
# Docente
# ======================
class Docente(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='app/docentes/', blank=True, null=True)
    link_lusofona = models.URLField(blank=True)

    def __str__(self):
        return self.nome

# ======================
# Unidade Curricular
# ======================
SEMESTRE_CHOICES = [
    (1, '1º Semestre'),
    (2, '2º Semestre'),
]

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    apresentacao = models.TextField()
    semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
    ects = models.IntegerField()
    licenciatura = models.ForeignKey(
        Licenciatura, on_delete=models.CASCADE, related_name='ucs'
    )
    docentes = models.ManyToManyField(Docente, related_name='ucs')
    imagem = models.ImageField(upload_to='app/ucs/',blank=True, null=True)

    def __str__(self):
        return self.nome


# ======================
# Projetos
# ======================
class Projeto(models.Model):
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='app/projetos/', blank=True, null=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.nome

# ======================
# Tecnologias
# ======================
TIPO_TECH_CHOICES = [
    ('linguagem', 'Linguagem'),
    ('framework', 'Framework'),
    ('bd', 'Base de Dados'),
    ('ferramenta', 'Ferramenta'),
]

NIVEL_CHOICES = [
    (1, 'Baixo'),
    (2, 'Médio'),
    (3, 'Alto'),
]

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_TECH_CHOICES)
    logo = models.ImageField(upload_to='app/tecnologias/', blank=True, null=True)
    link = models.URLField(blank=True)
    nivel_interesse = models.IntegerField(choices=NIVEL_CHOICES)

    def __str__(self):
        return self.nome

# ======================
# TFC
# ======================
class TFC(models.Model):
    nome = models.CharField(max_length=200)
    resumo = models.TextField()
    imagem = models.ImageField(upload_to='app/tfc/', blank=True, null=True)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, related_name='tfcs')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='tfcs')

    def __str__(self):
        return self.nome

# ======================
# Formação
# ======================
class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

# ======================
# Competências
# ======================
COMP_NIVEL_CHOICES = [
    (1, 'Básico'),
    (2, 'Intermédio'),
    (3, 'Avançado'),
]

class Competencia(models.Model):
    nome = models.CharField(max_length=200)
    nivel = models.IntegerField(choices=COMP_NIVEL_CHOICES)
    formacao = models.ForeignKey(Formacao, on_delete=models.CASCADE, related_name='competencias')
    tecnologia = models.ForeignKey(Tecnologia, on_delete=models.CASCADE, related_name='competencias')

    def __str__(self):
        return self.nome

# ======================
# MakingOf
# ======================
class MakingOf(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateField()
    imagem = models.ImageField(upload_to='app/makingof/', blank=True, null=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome