import django
from django import forms
from django.forms import ModelForm

from omg.models import TopicTable


class TopicForm(ModelForm):
    class Meta:
        model = TopicTable
        fields = ['topic','content']
        labels = {
            'topic': 'Topic',
            'content': 'Content',
        }
        widgets = {

            #'id': forms.HiddenInput,
        }

class FileForm(forms.Form):
    file = forms.FileField()