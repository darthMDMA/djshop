# Generated by Django 4.1.5 on 2023-02-10 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, help_text='не более 200 символов', max_length=200)),
                ('content', models.TextField(blank=True, help_text='не более 5000 символов', max_length=5000, null=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('discuss_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like_discussion', models.ManyToManyField(blank=True, related_name='discuss_like', to=settings.AUTH_USER_MODEL)),
                ('saves_discussion', models.ManyToManyField(blank=True, related_name='blog_discussion_save', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Обсуждение',
                'verbose_name_plural': 'Обсуждения',
            },
        ),
        migrations.DeleteModel(
            name='Discuss',
        ),
    ]
