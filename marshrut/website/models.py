import uuid

from django.db import models


# Create your models here.
class Clothes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), blank=False, editable=False, null=False)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    photo=models.ImageField(upload_to='photo/%Y/%m/%d',null=True)
