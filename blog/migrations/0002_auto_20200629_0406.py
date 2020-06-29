# Generated by Django 2.0 on 2020-06-29 07:06

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Very Low', max_length=25)),
                ('color', models.CharField(default='#cf0a2c', max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='migrated-post', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]