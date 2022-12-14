import random 
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL
# Create your models here.
class Share(models.Model):
    # maps to sql data
    user = models.ForeignKey(User, on_delete=models.CASCADE) # many users can own many tweets
    content = models.TextField(blank=True, null=True)
    image= models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id":self.id,
            "content":self.content,
            "likes": random.randint(0,299)
        }