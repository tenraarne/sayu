from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def content(request):
    return render(request, 'content.html')


def ideas(request):
    return render(request, 'ideas.html')

def join_us(request):
    return render(request, 'join_us.html')

def studio(request):
    return render(request, 'studio.html')