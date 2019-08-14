from django import forms
from .models import Board
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# class BoardForm(forms.Form):
#     title = forms.CharField(label="제목", widget=forms.TextInput(attrs={
#         'placeholder':'THE TITLE!'
#     }))
#     content = forms.CharField(label="내용",
#     error_messages = {'required':'제발 내용을 입력해주세요'},
#     widget=forms.Textarea(attrs={
#         'class':'Content-input',
#         'rows':5,
#         'cols':50,
#         'placeholder':'Fill the content'
        
#     }))

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'
        widgets= {'title' : forms.TextInput(attrs={
                                                'placeholder':'제목을 입력하세요.',
                                                'class':'title',}),
                'content': forms.Textarea(attrs={
                                                'placeholder':'내용을 입력하세요.',
                                                'class':'content',
                                                'rows':5,
                                                'cols':50,})}
        error_messages = {'title': {
                                'required':'제발 입력하세요',},
                        'content': {'required':'빈칸이 있습니다',},
                        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', '작성!'))