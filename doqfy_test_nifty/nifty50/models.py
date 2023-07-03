from django.db import models

class Nifty50Data(models.Model):
    # Add relevant fields for the data you want to store
    timestamp = models.DateTimeField()
    value = models.FloatField()
    
    def __str__(self):
        return f"Nifty 50 Data - {self.timestamp}"
