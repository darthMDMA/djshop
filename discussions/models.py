from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from django.template.defaultfilters import slugify
from django.urls import reverse


from django.utils import timezone


# Create your models here.


class Comment(models.Model):
    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, name='author', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    comment_content = models.TextField(max_length=5000,  help_text='не более 5000 символов') # для текста лучше не ставить null=True
    likes = models.ManyToManyField(User, related_name='comment_like', blank=True) # многие ко многим


    def total_likes(self): # для подсчета общего количества лайков
        return self. likes.count()


    def get_pk(self):
        return self.pk

    def get_author(self):
        return self.author


class Reply(models.Model):
    class Meta:
        verbose_name = 'Ответ на обсуждение'
        verbose_name_plural = 'Ответы на обсуждение'

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,  related_name='replies')
    author = models.ForeignKey(User, name='author', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    reply_content = models.TextField(max_length=5000, blank=False)
    like = models.ManyToManyField(User, related_name='reply_like', blank=True)


    def get_pk(self):
        return self.pk

    def get_author(self):
        return self.author
