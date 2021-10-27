from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_add=True)


def fetch_posts():
    pass
