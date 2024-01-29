from django.shortcuts import render

from .models import PaymentRequests, CompanyDetails


def index(request):
    template = 'reqtable/index.html'
    payreq = PaymentRequests.objects.all()
    context = {
        'page_obj': payreq,
    }
    return render(request, template, context)


def cominfo(request):
    template = 'reqtable/cominfo.html'
    cominfo = CompanyDetails.objects.all()
    context = {
        'page_obj': cominfo,
    }
    return render(request, template, context)
