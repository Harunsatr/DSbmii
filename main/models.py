from django.db import models

# Create your models here.
class bmii(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title
