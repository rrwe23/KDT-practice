# Generated by Django 3.2.13 on 2022-10-18 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=80),
        ),
    ]
