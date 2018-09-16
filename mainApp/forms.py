from django import forms
from .models import Events

class AddEventForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'The Event Name',
        }
    ))
    desciption = forms.CharField(widget=forms.Textarea(
        attrs={
            'class' : 'form-control'
        }
    ))
    link = forms.URLField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'The link of google forms',
        }
    ))
    last_date = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'type' : 'date',
        }
    ))
    class Meta:
        model = Events
        fields = ('title','desciption','link','pic','last_date')
