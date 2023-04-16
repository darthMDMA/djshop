import datetime

from django import forms
from jsonschema.exceptions import ValidationError

from .models import Comment, Reply


class DiscussionCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {  # перечень полей в которых мы меняем стиль
            'content': forms.Textarea(attrs={'style': 'resize: none;''width: 100%;''overflow: none;''height: 50px;'}),
        }

        labels = {
            'content': 'Добавить комментарий',

        }

    def cleaned_post_id(self):
        return self.cleaned_data['post_id']


class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        widgets = {  # перечень полей в которых мы меняем стиль
            'content': forms.Textarea(attrs={'style': 'resize: none;'
                                                      'width: 100%;'
                                                      'overflow: none;''height: 50px;'
                                                     }),
        }


#
class ContactForm(forms.Form):

    date_created = forms.DateField(initial=datetime.date.today())
    subject = forms.CharField(max_length=30 )
    message = forms.CharField(max_length=300)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=True)


    def clean_date_created(self):
        data = self.cleaned_data['date_created']
        today = datetime.date.today()
        if data != today:
            raise forms.ValidationError('Дата отправки должна быть сегодня')

        return data


