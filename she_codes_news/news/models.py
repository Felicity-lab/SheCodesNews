from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='published_stories')
    # author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()

    img_url=models.URLField(max_length=200, blank=True, null=True)
    # def __str__(self):
    #     return self.title + str(self.pub_date)

def __str__(self):
    return self.title