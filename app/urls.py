from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'), 
    path('tfcs/', views.tfcs_view, name='tfcs'), 
    path('docentes/', views.docentes_view, name='docentes'),
    path('/projetos/',views.projetos_view, name='projetos'),
    path('/projeto_novo/', views.projeto_novo_view, name='projeto_novo'),
]