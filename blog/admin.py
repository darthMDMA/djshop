from django.contrib import admin
from django.forms import TextInput, Textarea
from blog.models import *
from django.db import models


@admin.register(Post)   # добавили в админ панель свое приложение
class PageAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'date_created', 'date_updated', 'author']
    prepopulated_fields = {'slug': ('title',)}
    # def __str__(self):
    #     return self.title

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag, TagAdmin)


admin.site.site_title = 'Django practice'
admin.site.site_header = 'Админ-панель тренировочного сайта'