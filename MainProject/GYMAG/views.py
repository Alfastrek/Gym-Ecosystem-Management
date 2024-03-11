from django.shortcuts import render
from . import models
# Homepage
def home(request):
    banners=models.Banners.objects.all()
    services=models.Service.objects.all()[:3]
    return render(request,'home.html',{'banners':banners, 'services': services})

# PageDetail
def page_detail(request,id):
    page=models.Page.objects.get(id=id)
    return render(request,'page.html',{'page':page,})

# FAQ
def faq_list(request):
    faq=models.Faq.objects.all()
    return render(request,'faq.html',{'faq':faq,})    