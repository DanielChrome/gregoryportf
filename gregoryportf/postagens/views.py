from django.shortcuts import render_to_response, get_object_or_404, render
from postagens.models import Postagem, Categoria
from forms            import FormContato
from django.template  import RequestContext

# Create your views here.
def home(request):
    bemVindo = Postagem.objects.get(titulo='Bem vindo')
    java     = Postagem.objects.get(titulo='Java')
    django   = Postagem.objects.get(titulo='Django Framework')
    android  = Postagem.objects.get(titulo='Android')
    delphi   = Postagem.objects.get(categoria = 5)
    gpzim    = Postagem.objects.get(titulo='Gregory Pacheco')
    return render(request, 'postagens/index.html', locals())

def curriculo(request):
    curriculo    = Postagem.objects.get(titulo='Curriculo')
    apiJava      = Postagem.objects.get(titulo='API(s) Java')
    all_posts    = Postagem.objects.all()
    all_posts    = all_posts.filter(categoria = 2).order_by('pk')
    return render(request, 'postagens/curriculo.html',locals())
    
def deployedbyme(request):
    projetos    = Postagem.objects.all()
    projetos    = projetos.filter(categoria = 3).order_by('pk')
    return render(request, 'postagens/deployedbyme.html',locals())
    
def projetos(request):
    projetos    = Postagem.objects.all()
    projetos    = projetos.filter(categoria = 4).order_by('pk')
    return render(request, 'postagens/projetos.html',locals())

def contato(request):
    return render(request, 'postagens/contato.html',locals())

def contato(request):
    if request.method == "POST":
        form = FormContato(request.POST, request.FILES)
        if form.is_valid():
            contato = form.save(commit = False)
            contato.save()
            return render(request, 'postagens/contatosalvo.html',locals())
    else:
        form = FormContato()
    return render(request, 'postagens/contato.html',locals())