from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.template import loader
from sharoz_v1.models import Product, Photo, Suggestion


def home(request):
    template = loader.get_template('sharoz/home.html')

    context = {
        'latest_products': Product.objects.all().order_by('-pk')[:4]
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('sharoz/about.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


def suggest(request):
    template = loader.get_template('sharoz/suggest.html')

    context = {

    }
    return HttpResponse(template.render(context, request))


def single_product(request, product_id):
    template = loader.get_template('sharoz/single_product.html')

    context = {
        'Product': Photo.objects.all().get(pk=product_id),
    }
    return HttpResponse(template.render(context, request))


def products(request):
    template = loader.get_template('sharoz/products.html')

    context = {

        'Products1': Photo.objects.all()[0::3],
        'Products2': Photo.objects.all()[1::3],
        'Products3': Photo.objects.all()[2::3],

    }
    return HttpResponse(template.render(context, request))


def submit_suggestion(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        suggestion_model = Suggestion.objects.create()
        suggestion_model.name = name
        suggestion_model.email = email
        suggestion_model.message = message
        suggestion_model.save()
        return HttpResponseRedirect('/suggest/')
    else:
        return HttpResponse('bad request')
