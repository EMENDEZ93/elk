from django.shortcuts import render
from django.http import Http404
from .models import Language


def error_view(request):
    language = Language.objects.all()
    # raise Exception('error !!!!')
    # raise Http404("sorry 404")
    return render(request, 'django.html', {
        'data': "Hello Django ",
        'languages': language,
    })