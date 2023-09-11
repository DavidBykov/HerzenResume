from django.shortcuts import render


def index(request):
    template = 'MyResume/index.html'
    return render(request, template)