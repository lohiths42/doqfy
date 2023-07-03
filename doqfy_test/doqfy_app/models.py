from django.db import models
import shortuuid

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.short_url = shortuuid.uuid()[:]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_url
