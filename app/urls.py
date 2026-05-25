from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'), 
    path('tfcs/', views.tfcs_view, name='tfcs'), 
    path('docentes/', views.docentes_view, name='docentes'),
    path('projetos/',views.projetos_view, name='projetos'),
    path('projeto_novo/', views.projeto_novo_view, name='projeto_novo'),
    path('unidades/', views.unidades_view, name='unidades'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('makingOf/', views.makingOfs_view, name='makingOfs'),
    path('editar_projeto/<int:pk>/',views.editar_projeto, name='editar_projeto'),
    path('projeto/<int:pk>/apagar/', views.apagar_projeto, name='projeto_apagar'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('artigos/', views.artigos_view, name='artigos'),
    path('artigo_novo/', views.artigo_novo_view, name = 'artigo_novo'),
    path('comentario_novo/<int:pk>/', views.comentario_novo_view, name = 'comentario_novo'),
]