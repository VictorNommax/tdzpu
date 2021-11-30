from django.shortcuts import render
from django.urls import include
from .models import Products
from django.views.generic import DetailView
#import sqlite3

# Create your views here.
def getcontent(request, page='main'):

    total = Products.objects.all().count()

    if request.method=='GET' and request.GET.get('search'):
        keywords = str(request.GET.get('search'))
        products = Products.objects.filter(en__icontains = str(request.GET.get('mirrorsearch')))
        querywas = True
    else:
        products = Products.objects.all()
        keywords = ''
        querywas = False

    if page == 'main':
        title = 'Главная'
    elif page == 'about':
        title = 'О нас'
    else:
        title = 'Контакты'

    data = {
    'page':page,
    'title':title,
    'products' : products,
    'keywords':keywords,
    'querywas':querywas,
    'now':products.count(),
    'total':total
    }
    return render(request,'main/mainpage.html', data)

class ProductDetail(DetailView):
    model = Products
    template_name = 'main/product.html'
    context_object_name = 'theproduct'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        return context

def getabout(request):
    return getcontent(request, 'about')

def getcontacts(request):
    return getcontent(request, 'contacts')
