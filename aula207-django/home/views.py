from django.shortcuts import render

context = {
    'text': 'Estamos na home'
}


def home(request):
    return render(
        request,
        'home/index.html',
        context,
    )
