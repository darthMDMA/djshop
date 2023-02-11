from blog.models import Post
import pytest


@pytest.mark.django_db
def test_title_create():
    article = Post.objects.create(title='article1')
    assert article.title == 'article1'