from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('futsal shoes', 'Futsal shoes'),
        ('football shoes', 'Football shoes'),
        ('socks', 'Socks'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField(default="")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='football shoes')
    thumbnail = models.URLField(blank=True, null=True)
    sold_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_bestseller(self):
        return self.sold_count > 50
        
    def increment_sales(self):
        self.sold_count += 1
        self.save()


