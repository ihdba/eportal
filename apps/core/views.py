from django.shortcuts import render, redirect

# Create your views here.


def eportal(request):

    context = {
        'title': 'E-Portal',
    }

    return render(request, "core/eportal.html", context=context)