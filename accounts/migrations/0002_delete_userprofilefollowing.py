# Generated by Django 3.0.8 on 2020-07-10 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileFollowing',
        ),
    ]
