from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        # ferramentas
        widgets = {            
            'title': forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'titulo do comentario'}),

            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value':'', 'id':'user',
                'type':'hidden'
            }),

            'body' : forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'comentario'  
            })
        }