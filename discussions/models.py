from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

from django.utils import timezone


# Create your models here.


class Discussion(models.Model):
    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'
#
    title = models.CharField(max_length=200, help_text='не более 200 символов', db_index=True) # db_index добавляет индексацию и ускоряет поиск
    # content = models.TextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов') # для текста лучше не ставить null=True
    content = models.TextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов') # для текста лучше не ставить null=True
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото') # при добавлении фото путь в папках будет Год меся день
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, name='discuss_author', on_delete=models.CASCADE)
    # в urls.py при использовании slug добавлять id + get_absolute_url, если будет одинаковый slug у постов  unique=True
    slug = models.SlugField(max_length=50)
    like_discussion = models.ManyToManyField(User, related_name='discuss_like', blank=True) # многие ко многим
    saves_discussion = models.ManyToManyField(User, related_name='blog_discussion_save', blank=True) # один ко многим

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Discussion, self).save(*args,**kwargs)

    def total_likes(self): # для подсчета общего количества лайков
        return self. like_discussion.count()

    def get_absolute_url(self):
        return reverse('discuss-detail', kwargs={'pk': self.pk})
