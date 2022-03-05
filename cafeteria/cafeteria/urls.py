
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')),
    path('menu/', include('menu.urls')),
    path('admin/', admin.site.urls),
]
