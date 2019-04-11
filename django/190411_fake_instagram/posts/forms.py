from django import forms
from .models import Post
from crispy_forms.helper import FormHelper


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'