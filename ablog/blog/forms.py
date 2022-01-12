from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag','author','category', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'id_author','type':'hidden'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag','category','content']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            #author': forms.Select(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }