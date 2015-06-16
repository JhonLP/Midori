from django.contrib import admin
from models import Publicacion,Categoria

class PublicacionAdmin(admin.ModelAdmin):
	list_display = ('id','titulo', 'descripcion','categoria','votos','favoritos','usuario',)
	list_filter = ('categoria','usuario',)
	search_fields = ('categoria__titulo',)
	list_editable = ('titulo','descripcion','categoria', 'votos', 'favoritos',)
	list_display_links = ('id',)
	raw_id_fields = ('usuario',)


class PublicacionInline(admin.StackedInline):
	model = Publicacion
	extra = 1
	raw_id_fields = ('usuario',)

class CategoriaAdmin(admin.ModelAdmin):
	inlines = [PublicacionInline]


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Publicacion,PublicacionAdmin)
# Register your models here.
