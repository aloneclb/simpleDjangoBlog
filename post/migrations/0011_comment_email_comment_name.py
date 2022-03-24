# Generated by Django 4.0.1 on 2022-03-24 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_post_stand'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='asd', max_length=254, verbose_name='Kullanıcı E-maili:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='asd@asf.com', max_length=30),
            preserve_default=False,
        ),
    ]