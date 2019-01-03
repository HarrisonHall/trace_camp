from django import forms
from nasagram.models import NasaComment

# Create your models here.
class NasaCommentForm(forms.ModelForm):
    class Meta:
        model = NasaComment
        fields = ['comments','date','url','favorite','rating']
        widgets = {
            'url':forms.HiddenInput,
            'date':forms.HiddenInput,
        }

