from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Color(models.Model):
    color_name = models.CharField(max_length=20, default="Dark Red")
    rgb = models.CharField(max_length=8, default="#cf0a2c")

    def __str__(self):
        return self.color_name

class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    slug = models.CharField(max_length=200, default="migrated-post")
    color = models.ForeignKey("Color", on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
