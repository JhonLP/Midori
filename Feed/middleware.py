from actstream.actions import is_following

def es_favorito(request, post):
	return is_following(request.user,post)

class FavoritoMiddleware():
	def process_request(self, request):
		return es_favorito(request,post)