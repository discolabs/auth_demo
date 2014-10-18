from django.http import HttpResponse


def home(request, *args, **kwargs):
    return HttpResponse('Welcome to my application.')
