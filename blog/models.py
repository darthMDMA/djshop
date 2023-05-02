from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone



class Post(models.Model):
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'
#
    title = models.CharField(max_length=30, help_text='не более 200 символов', db_index=True) # db_index добавляет индексацию и ускоряет поиск
    content = models.TextField(max_length=5000, blank=False, null=False, help_text='не более 5000 символов') # для текста лучше не ставить null=True
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='photo') # при добавлении фото путь в папках будет Год меся день
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, related_name='post_tags',)
    slug = models.SlugField(max_length=50, db_index=True, verbose_name='URL')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True) # многие ко многим

    def __str__(self):
        return self.title

    def total_likes(self): # для подсчета общего количества лайков
        return self.likes.count()

    def total_comments(self):
        tot = 0
        for comment in self.comments.all():
            tot += 1
            for reply in comment.replies.all():
                tot += 1
        return tot

    def get_absolute_url(self):
        return reverse('post_url', kwargs={'username': self.author, 'post_slug': self.slug, 'post_id': self.id})


class Tag(models.Model):
    class Meta:
        verbose_name = 'Создать тэг'
        verbose_name_plural = 'Создать тэги'

    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_url', kwargs={'tag_slug': self.slug})

