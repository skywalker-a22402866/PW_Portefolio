from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'), 
    path('tfcs/', views.tfcs_view, name='tfcs'), 
]