from django.contrib import admin
from discussions.models import *


@admin.register(Comment)   # добавили в админ панель свое приложение
class DiscussAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'date_created', 'comment_content', ]


@admin.register(Reply)   # добавили в админ панель свое приложение
class RepliesAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'date_created', 'reply_content',]


