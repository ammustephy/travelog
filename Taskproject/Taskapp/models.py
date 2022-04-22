from django.db import models

# Create your models here.
class Images(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    post=models.TextField()

    def __str__(self):
        return self.name