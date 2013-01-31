# -*- coding: utf8 -*-
from django.contrib import admin
from gregoryportf.postagens.models import Postagem, Categoria, Contato

class PostagemAdmin(admin.ModelAdmin):
	# Alterando a ordem dos campos
	fields = ['titulo', 'datapublicacao', 'usuario', 'conteudo', 'categoria', 'imagem']

admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Categoria)
admin.site.register(Contato)
