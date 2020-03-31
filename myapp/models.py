from django.db import models

class user(models.Model):
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100, default = 'Kapurthala')
    phone = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
