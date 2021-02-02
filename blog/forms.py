from django import forms
from .models import Comment
from .import models

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.Form):
    model = Comment
    fields = ('name','email','body')

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','slug','author','body']
