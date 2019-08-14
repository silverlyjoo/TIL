from django import forms
from .models import Movie, Score

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 5,
                'cols': 10,
            }),
            'poster_url': forms.Textarea(attrs={
                'rows': 5,
                'cols': 50,
            }),
            
        }


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['score', 'content',]
        widgets = {
            'score': forms.NumberInput(attrs={
                'step':1,
                'max':5,
                'min':1,
            })
        }