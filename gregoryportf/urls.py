from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", "postagens.views.home", name="home"),
  # url(r"^$", direct_to_template, {"template": "homepage.html", }, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^curriculo/$", "postagens.views.curriculo", name="curriculo"),
    url(r"^deployedbyme/$", "postagens.views.deployedbyme", name="deployedbyme"),
    url(r"^projetos/$", "postagens.views.projetos", name="projetos"),
    url(r"^contato/$", "postagens.views.contato", name="contato"),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )


