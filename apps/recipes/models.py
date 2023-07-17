from django.db import models

# Create your models here.


class Recipe(models.Model):

    name = models.CharField(max_length=120)
    recipe = models.TextField()
    image = models.ImageField(upload_to='recipes/')


    def __str__(self):

        return f"{self.name}"

    class Meta:

        verbose_name_plural = "Recipes"