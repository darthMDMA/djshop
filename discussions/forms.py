from django import forms
from jsonschema.exceptions import ValidationError

from .models import Discussion


class DiscussionCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): # конструктор экзмепляра класса форм
        self.author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs) # вызов конструктора базового класса


    class Meta:
        model = Discussion
        fields = ['title', 'content']
        widgets = {  # перечень полей в которых мы меняем стиль
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }


    def clean_title(self): # Валидатор для проверки поля Заголовок. начинается с clean!!!
        title = self.cleaned_data['title'] # получаем даныне по заголовку
        if len(title) > 200: # Если длинна больше 200
            raise ValidationError('Длинна превышает 200 символов') # генерация исключения
        return title # либо возвращение заголовка




