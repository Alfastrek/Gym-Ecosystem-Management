from django.shortcuts import render
from . import models

def home(request):
    banners=models.Banners.objects.all()
    services=models.Service.objects.all()[:3]
    return render(request,'home.html',{'banners':banners, 'services': services})

# Create your views here.
def page_detail(request,id):
    page=models.Page.objects.get(id=id)
    return render(request,'page.html',{'page':page,})