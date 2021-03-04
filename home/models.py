from django.db import models

GENDER_CHOICES = (
    ('M','Muž'),
    ('F', 'Žena'),
)

class HomeData(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    azure_key = models.CharField(max_length=100)
    azure_end = models.CharField(max_length=100)
    wit_key = models.CharField(max_length=100)
    weather_key = models.CharField(max_length=100)
    bridge_ip = models.CharField(max_length=100)
    voice = models.CharField(max_length=2, choices=GENDER_CHOICES, default='M')
