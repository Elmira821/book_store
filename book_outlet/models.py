from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=50)  
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    
    def __str__(self):           #it's a method.   so we can read object easily
        return f"{self.title} ({self.rating})"
    
    
    