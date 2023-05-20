from django.db import models

# Create your models here.

class Topics(models.Model):
    topic_name=models.CharField(max_length=200)

    def __str__(self):
        return self.topic_name
    
class Article(models.Model):
    topic=models.ForeignKey(Topics,on_delete=models.CASCADE,related_name='articles')
    tittle= models.CharField(max_length=200)
    article=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    image_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics/')
    def __str__(self):
        return self.tittle


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)