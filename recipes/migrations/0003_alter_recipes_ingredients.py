# Generated by Django 3.2.3 on 2021-06-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210624_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='ingredients',
            field=models.TextField(max_length=500),
        ),
    ]
