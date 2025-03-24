from django.db import models

class CategoryKino(models.Model):
    categorykino = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.categorykino
class CategoryDavlati(models.Model):
    categorydavlati = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.categorydavlati
    
class CategoryTili(models.Model):
    categorytili = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.categorytili
    
class CategoryYili(models.Model):
    categoryyili = models.CharField(max_length=100, null=True)    
    def __str__(self):
        return self.categoryyili
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='media/')
    categorykinolar = models.ForeignKey(CategoryKino, blank=True, null=True, on_delete=models.SET_NULL)
    categorydavlati = models.ForeignKey(CategoryDavlati, blank=True, null=True, on_delete=models.SET_NULL)
    categorytili = models.ForeignKey(CategoryTili, blank=True, null=True, on_delete=models.SET_NULL)
    categoryyili = models.ForeignKey(CategoryYili, blank=True, null=True, on_delete=models.SET_NULL)
    davomiyligi = models.CharField(max_length=100, null=True)
    
    