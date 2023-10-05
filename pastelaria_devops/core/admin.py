from django.contrib import admin
from .models import Produto
from .models import Venda
from .models import ProdutoVenda

# Register your models here.

admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(ProdutoVenda)