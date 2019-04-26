# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import formset_factory, modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from taamcru.forms import GunDamForm
from taamcru.models import GunDamTable


def create(request):
    add_model = GunDamTable(name='Gaiking',hp='4000')
    add_model.save()
    return HttpResponse('Add finish')

def show(request):
    showlist = GunDamTable.objects.filter(name='Gaiking')
    for row in showlist:
        print row.name+" " +str(row.hp)
    return HttpResponse('Show')

def myformset(request):
    name = 'Gaiking'
    Hengformset = modelformset_factory(GunDamTable,form=GunDamForm,extra=0)
    gundam_model = GunDamTable.objects.filter(name=name)
    hengformset = Hengformset(queryset=gundam_model)
    return render(request,'showform_page.html',{'hengformset':hengformset})
