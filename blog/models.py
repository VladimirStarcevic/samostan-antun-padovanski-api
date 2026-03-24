from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):

   class Status(models.TextChoices):
       DRAFT = "DF", "Nacrt"
       PUBLISHED = "PB", "Objavljeno"

   title = models.CharField(max_length=250)
   slug = models.SlugField(max_length=250, unique=True)
   body = models.TextField()

   author = models.ForeignKey(
       settings.AUTH_USER_MODEL,
       on_delete=models.CASCADE,
       related_name='blog_posts',
   )

   publish = models.DateTimeField(default=timezone.now)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)

   status = models.CharField(
       max_length=2,
       choices=Status,
       default=Status.DRAFT,
   )

   tags = models.ManyToManyField(Tag, blank=True)

   class Meta:
       ordering = ['-publish']
       indexes = [
           models.Index(fields=['-publish']),
       ]
   def __str__(self):
       return self.title