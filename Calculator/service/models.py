from django.db import models

class Services(models.Model):
    
    # Define the Number of fields
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_desc = models.TextField()
