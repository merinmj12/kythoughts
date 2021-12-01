from .models import Task
from django import forms


class Kuttyforms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'desc', 'date']
