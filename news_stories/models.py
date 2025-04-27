from django.db import models
from django.utils.text import slugify

class Story(models.Model):  # Capital "S"
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    image_url = models.URLField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title