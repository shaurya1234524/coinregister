from django.db import models
class Coin(models.Model):
    name=models.CharField(max_length=120,default="Error 404")
    image=models.ImageField(default="Error 404",upload_to='image/')
    description=models.TextField(default="Error 404")
    url=models.URLField( max_length=200,default="Error 404")
    def __str__(self):
        return self.name
# Create your models here.
