from django.shortcuts import render
from .models import Clothes


# Create your views here.
def index(request):
    dataClothes=Clothes.objects.all()
    context={
       'data': dataClothes
    }
    return render(request, 'website/index.html',context)


def about(request):
    return render(request, 'website/aboutus.html')
