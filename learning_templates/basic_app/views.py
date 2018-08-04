from django.shortcuts import render

# Create your views here.


def index(request):
    ctx = {'text': 'hello world', 'number': 100}
    return render(request, 'basic_app/index.html', context=ctx)


def other(request):
    return render(request, 'basic_app/other.html')


def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
