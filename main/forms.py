from django import forms
from .models import bmii

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = bmii
        fields = ('title', 'file')
