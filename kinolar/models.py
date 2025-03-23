from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.category

# Janr modeli
class Genre(models.Model):
    janiri = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.janiri

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies')
    janiri = models.ManyToManyField(Genre, related_name='movies')
    video_file = models.FileField(upload_to='media/', blank=True, null=True)
    
    
    

    
    def __str__(self):
        return self.title
