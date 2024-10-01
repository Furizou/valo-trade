from django.db import models
from django.contrib.auth.models import User
import uuid  # tambahkan baris ini di paling atas

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    time = models.DateField(auto_now_add=True)
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()