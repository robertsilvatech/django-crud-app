from django.urls import path
from .views import novo_produto_view
from .views import listar_produtos_view
from .views import editar_produtos_view
from .views import deletar_produtos_view

urlpatterns = [
    path('produto', novo_produto_view, name='novo_produto'),
    path('produto/<id>', editar_produtos_view, name='editar_produto'),
    path('produto/<id>/delete', deletar_produtos_view, name='deletar_produto'),
    path('produtos', listar_produtos_view, name='lista_produtos')
]

