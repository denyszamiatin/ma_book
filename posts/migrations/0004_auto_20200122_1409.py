# Generated by Django 3.0.2 on 2020-01-22 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_hashtag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='hashtag',
            new_name='hash_tag',
        ),
    ]
