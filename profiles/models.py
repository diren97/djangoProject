from datetime import datetime
from django.contrib.auth.models import User
from django.dispatch import  receiver
from django.db import models
from django.db.models.signals import post_save

choices = [(i,i) for i in range(1900, datetime.now().year+1)]
cities = (('54','Sakarya'),('48','Mugla'),('26','Eskisehir'))

class Profile(models.Model):
    user = models.OneToOneField(to ='auth.User',on_delete=models.CASCADE)
    picture = models.ImageField(blank=True)
    city = models.CharField(choices = cities,max_length=20)

    def __str__(self):
        return f"{self.user.username}'nin profili"

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()