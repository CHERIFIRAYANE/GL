# Generated by Django 4.1.4 on 2022-12-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espaceannonce', '0002_annonce'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='date_modif',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
