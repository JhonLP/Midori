from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from Feed.views import PublicacionListView, PublicacionDetailView

from django.contrib import admin


urlpatterns = patterns(
    "",
    url(r"^$", 'Feed.views.home', name="home"),
    url(r'^categoria/(\d+)$', 'Feed.views.categoria', name='categoria'),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^favoritos/", include("favorites.urls")),
    url(r'^feed/$', PublicacionListView.as_view(), name='publicaciones'),
    url(r'^feed/(?P<pk>[\d]+)$', PublicacionDetailView.as_view(), name='publicaciones'),
    url(r'^usuario/(\d+)$', 'Feed.views.usuario', name='usuario'),
    url(r'^activity/', include('actstream.urls')),
    url(r'^seguir/(?P<id_usuario>\d+)$', 'Feed.views.seguir', name='seguir'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
