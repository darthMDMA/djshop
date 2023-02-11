from django import forms
from .models import *
from .utils import django_slugify
from django.contrib.auth.models import User


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo',]

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        # if Post.objects.filter(slug__iexact=new_slug).count():
        #     raise ValueError('slug must be unique')
        return new_slug

    #
