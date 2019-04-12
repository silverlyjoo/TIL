from django import forms
from .models import Post, Image
from crispy_forms.helper import FormHelper


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', ]
        
        widgets = {
            'file':forms.FileInput(attrs={'multiple':True}),
        }