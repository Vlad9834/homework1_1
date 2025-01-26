from django.shortcuts import render

from homeproject.models import AutoModel


def index(request):
    return render(request,"homeproject/index.html")

def products(request):
    cars = AutoModel.objects.all()
    context = {
        "cars":cars,

    }

    return render(request,"homeproject/products.html",context=context)

def show_product(request,car_id):
    car = AutoModel.objects.get(id=car_id)
    context = {
        "car":car

    }


    return render(request,"homeproject/show_product.html",context=context)

