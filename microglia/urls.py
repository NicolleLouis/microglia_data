from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def home(request):
    context = {
        "title": "Home"
    }
    return render(request, "microglia/home.html", context)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('data_storage/', include("data_storage.urls"))
]
