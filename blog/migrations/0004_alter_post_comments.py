# Generated by Django 4.1.5 on 2023-02-20 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0002_comment_reply_delete_discussion_comment_replies'),
        ('blog', '0003_post_comments_alter_post_content_alter_post_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='discussions.comment'),
        ),
    ]
