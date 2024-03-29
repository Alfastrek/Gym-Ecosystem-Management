from django.db import models
from django.utils.html import mark_safe


#banners
class Banners(models.Model):
    img = models.ImageField(upload_to='D:\gympro\myprojectenv\GYMAG\media\banners/')
    alt_text = models.CharField(max_length=150)
    
    def __str__(self):
        return self.alt_text


    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))
# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img=models.ImageField(upload_to = "services/", null=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))    
    
class Page(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField()

    def __str__(self):
        return self.title 

class Faq(models.Model):
    quest=models.TextField()
    ans=models.TextField()

    def __str__(self):
        return self.quest