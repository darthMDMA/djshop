from django import forms
from .models import Post

# узнать как применить в форме  fileds initital, для класса Form
# для класса форм это делается forms.DateField(initital=datetime.date.toda)
# так же разобраться как cleaned_data Обрабатывает поля форм
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'photo']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 100%;'}),
                   'content': forms.Textarea(attrs={'style': 'resize: none;' 
                                                             'width: 100%;'
                                                             'min-width: 344px;'
                                                             'overflow: none;'
                                                             'height: auto;'}),
                   'tags': forms.CheckboxSelectMultiple(),}

        labels = {'title': 'Название статьи',
                  'content': 'Содержание',
                  'tags': 'Тэги',
                  'photo': 'Картинка', }

    def slug_cleaned(self):
        return self.cleaned_data['slug']


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'photo']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input', 'style': 'width: 100%;'}),
                   'content': forms.Textarea(attrs={'style': 'resize: none;' 
                                                             'width: 100%;'
                                                             'min-width: 344px;'
                                                             'overflow: none;'
                                                             'height: auto;'}),
                   'tags': forms.CheckboxSelectMultiple(),}

        labels = {'title': 'Название статьи',
                  'content': 'Содержание',
                  'tags': 'Тэги',
                  'photo': 'Картинка', }
