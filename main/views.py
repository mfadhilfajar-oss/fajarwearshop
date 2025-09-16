from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductsForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products_list = Product.objects.all()

    context = {
        'name': 'Muhammad Fadhil Al Afifi Fajar',
        'class': 'PBP C',
        'products_list': products_list
    }

    return render(request, "main.html", context)

def create_products(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)

def show_products(request, id):
    products = get_object_or_404(Product, pk=id)
    products.increment_sales()

    context = {
        'products': products
    }

    return render(request, "products_detail.html", context)

    
def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")
 
def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, products_id):
    try: 
        product_item = Product.objects.filter(pk=products_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request,  products_id):
    try:
        product_item = Product.objects.get(pk=products_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
       return HttpResponse(status=404)