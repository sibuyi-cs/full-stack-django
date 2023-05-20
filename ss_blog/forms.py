from django import forms
from .models import Topics,Article,Comment
      
class Topic_form(forms.ModelForm):
    class Meta():
        model=Topics
        fields=("topic_name",) 
         
class Article_form(forms.ModelForm):
    class Meta():
        model=Article
        exclude=["created_at",]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
