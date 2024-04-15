from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile')
    
    def __str__(self):
        return  f"{self.user.username} Profile"
    """
    method already exist in parent class 
    and runs every time after out model is save.
    resizing image
    """
    def save(self):
        super().save()
        #open the image of current instance
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
