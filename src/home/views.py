from django.http import Http404
from django.shortcuts import render
from .models import Product, ProductImage


def index(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "index.html", context)


def single_product(request, slug):
    try:
        products = Product.objects.get(slug=slug)
        images = products.productimage_set.all()

    except:
        raise Http404

    context = {
        "products": products,
        "images" :images,
    }
    return render(request, "product.html", context)

def search(request):
    print(request.GET.get("search_input"))
    context = {}
    return render(request,"index.html",context)
