from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    image = models.ImageField(blank=True)
    header = models.CharField(max_length=30)
    content = models.TextField(max_length=30000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(blank=True)
    owner = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='articles')

    def publish(self):
        if self.draft:
            self.drafg = False
        else:
            self.draft = True
        self.save()

    def __str__(self):
        return self.header

class Comment(models.Model):
    header= models.CharField(max_length=30)
    content = models.TextField(max_length=30000)
    owner = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(to=Article,on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header



