# -*- coding: utf8 -*-
from django.contrib import admin
from gregoryportf.postagens.models import Postagem, Categoria, Contato

admin.site.register(Postagem)
admin.site.register(Categoria)
admin.site.register(Contato)
