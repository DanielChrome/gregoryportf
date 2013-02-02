# -*- coding: utf8 -*-
from django.contrib import admin
from gregoryportf.postagens.models import Postagem, Categoria, Contato

class PostagemAdmin(admin.ModelAdmin):
	# Alterando a ordem dos campos
        fieldsets = [
            ('Dados da postagem', {'fields':['titulo', 'datapublicacao', 'usuario', 'conteudo', 'categoria', 'imagem']}),
	]
        list_display   = ('titulo', 'datapublicacao', 'usuario', 'categoria') # O Django deixa vc ordenar por cada um destes
        list_filter    = ['titulo', 'datapublicacao', 'usuario', 'categoria'] # Ativa um filtro fooodaa do lado direito
        search_fields  = ['titulo', 'id'] # Ativa a pesquisa fooddaa que pesquisa por varias coisas ao mesmo tempo
        date_hierarchy = 'datapublicacao'
        
class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados da categoria', {'fields': ['nome']}),
    ]
    
    list_display   = ('nome', 'id') # O Django deixa vc ordenar por cada um destes
    list_filter    = ['nome'] # Ativa um filtro fooodaa do lado direito
    search_fields  = ['nome', 'id'] # Ativa a pesquisa fooddaa que pesquisa por varias coisas ao mesmo tempo

admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contato)
