# Generated by Django 4.0.1 on 2022-03-24 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='stand',
            field=models.BooleanField(default=True, verbose_name='Öne çıkarılsın mı?'),
        ),
    ]
