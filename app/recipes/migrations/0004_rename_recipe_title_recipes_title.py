# Generated by Django 3.2.3 on 2021-06-24 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipes_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='recipe_title',
            new_name='title',
        ),
    ]