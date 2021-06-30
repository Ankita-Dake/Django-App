from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, From app. You're at the myapp index.")


def home(request):
    return HttpResponse("Hello, From app. You are at the myapp Home")


def about(request):
    return HttpResponse("Hello, From app. You are at the myapp About")


def contact(request):
    return HttpResponse("Hello From app. Yor are at the myapp contact")
