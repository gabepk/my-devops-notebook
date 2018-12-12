from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        # author eh a pessoa logada
        # created_date eh a data atual
        fields = ('title', 'text')