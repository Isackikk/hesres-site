from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='http://127.0.0.1:5500/frontend/html/home.html')),
    path('admin/', admin.site.urls),
    path('api/', include('loja.urls')),
]