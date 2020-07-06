from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class KnowledgeLevel(models.Model):
    name = models.CharField(max_length=25, default="Very Low")
    color = models.CharField(max_length=8, default="#cf0a2c")
    knowledge_level_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    slug = models.CharField(max_length=200, default="migrated-post")
    #knowledge_level = models.ForeignKey("KnowledgeLevel", blank=True, null=True, default=1, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
