from django.shortcuts import render

# Create your views here.



def partners(request):

    context = {
        'title': "Partners",
    }

    return render(request, 'partners/partners.html', context=context)