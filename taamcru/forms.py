import django
from django.forms import ModelForm

from taamcru.models import GunDamTable


class GunDamForm(ModelForm):
    class Meta:
        model = GunDamTable
        fields = ['name','hp']
        labels = {
            'name': 'Name',
            'hp' : 'HP',
        }