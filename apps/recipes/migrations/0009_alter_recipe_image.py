# Generated by Django 4.2.3 on 2023-07-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='images/recipes/greek-food.jpeg', upload_to='images/recipes/'),
        ),
    ]
