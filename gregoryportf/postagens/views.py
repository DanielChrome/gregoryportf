from django.shortcuts import render_to_response, get_object_or_404, render
from postagens.models import Postagem

# Create your views here.
def home(request):
	bemVindo = Postagem.objects.get(titulo='Bem vindo')
	java     = Postagem.objects.get(titulo='Java')
	django   = Postagem.objects.get(titulo='Django Framework')
	android  = Postagem.objects.get(titulo='Android')
	delphi   = Postagem.objects.get(titulo='Delphi')
	gpzim    = Postagem.objects.get(titulo='Gregory Pacheco')
	return render(request, 'postagens/index.html', locals())

def curriculo(request):
	curriculo    = Postagem.objects.get(titulo='Curriculo')
	apiJava      = Postagem.objects.get(titulo='API(s) Java')
	return render(request, 'postagens/curriculo.html',locals())

