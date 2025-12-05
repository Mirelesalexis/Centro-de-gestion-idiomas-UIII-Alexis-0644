from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('academia/', include('academia.urls')),
    path('', RedirectView.as_view(url='/academia/', permanent=True)),  # Redirige la raíz a /academia/
]
