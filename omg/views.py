# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
import omg
# Create your views here.
from omg.forms import TopicForm, FileForm
from omg.models import TopicTable


def index(request):
    return render(request,'index.html')


def show_topic(request):
    room_id = request.GET['room_id']
    same_room_data = TopicTable.objects.filter(room_id=room_id)
    return render(request,'show_topic_page.html',{'room_id':room_id,'same_room_data':same_room_data})





def add_topic1(request):

    if request.method=="GET":
        room_id = request.GET['room_id']
        addform = TopicForm()
    elif request.method == "POST":
        addform = TopicForm(request.POST)
        room_id = request.POST['room_id']

        if addform.is_valid():

            add_topic = addform.cleaned_data['topic']
            add_content = addform.cleaned_data['content']

            heng = TopicTable(room_id=room_id, topic=add_topic, content=add_content)
            heng.save()
            print 'add finish'
        where = '/show_topic?room_id='+str(room_id)
        return redirect(where)
    return render(request,'add_topic_page.html', {'addform':addform,'room_id':room_id })

def edit_topic(request):

    if request.method == "POST":

        topic_id = request.POST['topic_id']
        editmodel = TopicTable.objects.get(id=topic_id)
        room_id = editmodel.room_id
        editform = TopicForm(request.POST,instance=editmodel)
        if editform.is_valid():

            editform.save()

            # heng_editform = editform.save(commit=False)
            # room_id = heng_editform.room_id
            # heng_editform.save()

            # topic = editform.cleaned_data['topic']
            # content = editform.cleaned_data['content']
            # editmodel = TopicTable.objects.get(id=topic_id)
            # editmodel.topic = topic
            # editmodel.content = content
            # room_id = editmodel.room_id
            # editmodel.save()



        where = '/show_topic?room_id='+str(room_id)
        return redirect(where)

    topic_id = request.GET['topic_id']
    editmodel = TopicTable.objects.get(id=topic_id)
    editform = TopicForm(instance=editmodel)
    room_id = editmodel.room_id

    return render(request,'edit_topic_page.html', {'edit_form':editform,'topic_id':topic_id})

def testform(request):
    HengFormSet = modelformset_factory(TopicTable, form=TopicForm,extra=0)

    hengmodel = TopicTable.objects.filter(topic="ss")
    hengformset = HengFormSet(queryset=hengmodel)
    return render(request, 'show_formset.html',{'hengformset':hengformset})


def handle_uploaded_file(f):
    with open('omg/media/sheet1.xls', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def testfile(request):
    if request.method == "POST":
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
        return HttpResponse('add finish')
    fileform = FileForm()
    return render(request,'fileform_page.html',{'fileform':fileform})


def testgest(request):
    return HttpResponse('testheng')







