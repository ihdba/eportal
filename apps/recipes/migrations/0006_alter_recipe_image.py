# Generated by Django 4.2.3 on 2023-07-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='fasolatha-greek-food.jpeg', upload_to='images/recipes/'),
        ),
    ]
