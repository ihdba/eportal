# Generated by Django 4.2.3 on 2023-07-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='fasolatha-greek-food.jpeg', upload_to='media/images/recipes/'),
        ),
    ]
