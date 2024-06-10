from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products/')
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updates_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name
    
    def edit(self, name, description, image):
        self.product_name = name
        self.product_description = description
        self.product_image = image
        self.save()
        
    def short_description(self):
        words = self.product_description.split()
        
        if len(words) > 50:
            return ' '.join(words[:30]) + '....'
        else:
            return self.product_description
        
        