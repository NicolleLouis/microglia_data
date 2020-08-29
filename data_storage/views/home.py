from django.shortcuts import render


def home(request):
    context = {
        "title": "Home"
    }
    return render(request, "data_storage/home.html", context)
