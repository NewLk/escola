from django.urls import path
from . views import CursoAPIView, AvaliacaoAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='Cursos'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='Avaliacoes')
]