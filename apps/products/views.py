from django.shortcuts import render

# Create your views here.


def products(request):
    context = {
        'title': 'Products',
    }
    return render(request, "products/products.html", context=context)