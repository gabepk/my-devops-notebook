from django.contrib import admin
from .models import KnowledgeLevel
from .models import Post

# Register your models here.
admin.site.register(KnowledgeLevel)
admin.site.register(Post)
