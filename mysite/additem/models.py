from django.db import models

def upload_to(instance, filename):
    # Use instance attributes to define the path
    return f"members/{instance.item_id}/{filename}"
# Create your models here.
class Member(models.Model):
    item_name  = models.CharField(max_length=50)
    link  = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_path = models.CharField(max_length=50)
    item_id = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_to)

     