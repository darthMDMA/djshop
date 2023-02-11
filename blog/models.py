from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'
#
    title = models.CharField(max_length=200, help_text='не более 200 символов', db_index=True) # db_index добавляет индексацию и ускоряет поиск
    # content = models.TextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов') # для текста лучше не ставить null=True
    content = models.TextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов') # для текста лучше не ставить null=True
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='photo') # при добавлении фото путь в папках будет Год меся день
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # в urls.py при использовании slug добавлять id + get_absolute_url, если будет одинаковый slug у постов  unique=True
    slug = models.SlugField(max_length=50, db_index=True, verbose_name='URL')
    likes = models.ManyToManyField(User, related_name='postcomment', blank=True) # многие ко многим
    reply = models.ForeignKey('self', blank=True, null=True, related_name='reply_ok', on_delete=models.CASCADE) # один ко многим

    def __str__(self):
        return self.title

    def total_likes(self): # для подсчета общего количества лайков
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post', kwargs={'username': self.author, 'post_slug': self.slug, 'post_id': self.id})

