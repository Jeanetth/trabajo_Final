from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ans/', include('metodos.urls')),
    path('admin/', admin.site.urls),
]
