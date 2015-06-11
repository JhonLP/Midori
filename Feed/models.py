from django.db import models
from account.compat import AUTH_USER_MODEL

# Create your models here.

class Categoria(models.Model):
	titulo = models.CharField(max_length = 140)

	def __unicode__(self):
		return self.titulo

class Publicacion(models.Model):
	titulo = models.CharField(max_length = 140)
	votos = models.IntegerField(default = 0)
	favoritos = models.IntegerField(default = 0)
	categoria = models.ForeignKey(Categoria)
	usuario = models.ForeignKey(AUTH_USER_MODEL)
	timestamp = models.DateTimeField(auto_now_add = True)
	imagen = models.ImageField(upload_to='media/', blank=True, null=True)

	def __unicode__(self):
		return self.titulo



class Huerto(models.Model):
	titulo = models.CharField(max_length = 140)
	seguidores = models.IntegerField(default = 0)
	usuario = models.ForeignKey(AUTH_USER_MODEL)
