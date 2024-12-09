
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # registrar urls de nuestra aplicacion movies
    url(r'^', include('apps.movies.urls'))
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

