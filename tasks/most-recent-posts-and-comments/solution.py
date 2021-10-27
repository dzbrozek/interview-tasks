from django.db import models
from django.db.models import Window, F, Subquery, OuterRef, Prefetch
from django.db.models.functions import Rank, RowNumber
from django_cte import CTEManager, With


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_add=True)

    objects = CTEManager()  # required only for second solution


def first_solution():
    subquery = Comment.objects.filter(post=OuterRef('post')).order_by('-created_at')
    comments = Comment.objects.filter(
        pk__in=Subquery(subquery.values('pk')[:2])
    ).order_by('-created_at')
    return Post.objects.all().prefetch_related(Prefetch('comments', queryset=comments))


def second_solution():
    cte = With(
        Comment.objects.all().annotate(
            position=Window(
                expression=RowNumber(),
                partition_by=[F('post')],
                order_by=F('created_at').desc(),
            ),
        )
    )

    return Post.objects.all().prefetch_related(
        Prefetch('comments', queryset=cte.queryset().with_cte(cte).filter(position__lte=2))
    )
