from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from datetime import datetime
from models import *
from django.shortcuts import get_object_or_404
#from forms import *
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from account.models import Account

class PublicacionListView(ListView):
	model = Publicacion
	context_object_name = 'publicaciones'
	def get_template_names(self):
		return 'index.html'

class PublicacionDetailView(DetailView):
	model = Publicacion
	def get_template_names(self):
		return 'publicacion.html'	

def home(request):
	categorias = Categoria.objects.all()
	publicaciones = Publicacion.objects.order_by("-votos").all()[:15] #limita a 50 resultados
	template = "index.html"
	return render(request,template,locals())	

def categoria(request,id_categoria):
	categorias = Categoria.objects.all()
	categoria = get_object_or_404(Categoria, pk=id_categoria)
	publicaciones = Publicacion.objects.filter(categoria = categoria)
	template = "index.html"
	return render(request,template,locals())

@login_required
def plus(request, id_publicacion):
	enlace = Enlace.objects.get(pk=id_publicacion)
	enlace.votos = enlace.votos + 1
	enlace.save()
	return HttpResponseRedirect("/feed")

def usuario(request,id_usuario):
	categorias = Categoria.objects.all()
	usuario = Account.objects.get(pk=id_usuario)
	publicaciones = Publicacion.objects.filter(usuario = id_usuario)
	template = "user.html"
	return render(request,template,locals())