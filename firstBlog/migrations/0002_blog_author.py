# Generated by Django 4.0.5 on 2022-07-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
