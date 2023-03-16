from django.urls import path
from . views import CursosAPIView, CursoAPIView, AvaliacoesAPIView, AvaliacaoAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='Cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='Avaliacoes'),
    path('curso/<int:pk>/', CursoAPIView.as_view(), name='Curso'),
    path('avaliacao/<int:pk>/', AvaliacaoAPIView.as_view(), name='Avaliacao')
]