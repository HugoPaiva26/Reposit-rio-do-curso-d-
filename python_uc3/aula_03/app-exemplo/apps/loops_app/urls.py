from django.urls import path
from . import views


app_name = "loops" #aula_03


urlpatterns = [
    path('', views.index, name='index'), #aula_03
    path('for/', views.pagina_for, name='pagina_for'),
    path('jogo/', views.jogo_adivinhacao, name='jogo_adivinhacao'),
]