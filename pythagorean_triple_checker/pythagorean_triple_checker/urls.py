from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('triple_checker.urls')),
    path('admin/', admin.site.urls),
]