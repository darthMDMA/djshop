from django.contrib import admin
from django.forms import TextInput, Textarea

from django.db import models
from discussions.models import Discussion
# Register your models here.


@admin.register(Discussion)   # добавили в админ панель свое приложение
class DiscussAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'date_created', 'date_updated', 'discuss_author']
    prepopulated_fields = {'slug': ('title',)}
    # def __str__(self):
    #     return self.title

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

# admin.site.register(Post, PageAdmin)