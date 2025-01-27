from django.http import HttpResponse
from django.shortcuts import render

from homeproject.models import AutoModel


menu = [
    {"url":"shop","name":"каталог"},
    {"url":"add_car","name":"Добавить авто"},
    {"url":"contacts","name":"контакты"},
    {"url":"login","name":"логин"},

]

def add_car(request):
    context = {"menu": menu}
    return render(request,"homeproject/add_car.html",context)

def contacts(request):
    context = {"menu": menu}
    return render(request,"homeproject/contacts.html",context)

def login(request):
    context = {"menu": menu}
    return render(request,"homeproject/login.html",context)


def index(request):
    context = {"menu":menu}
    return render(request,"homeproject/index.html",context=context)

def products(request):
    cars = AutoModel.objects.all()
    context = {
        "cars":cars,
        "menu":menu,

    }

    return render(request,"homeproject/products.html",context=context)

def show_product(request,car_id):
    car = AutoModel.objects.get(id=car_id)
    context = {
        "car":car,
        "menu": menu,

    }


    return render(request,"homeproject/show_product.html",context=context)

